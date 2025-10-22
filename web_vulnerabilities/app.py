# File: web_vulnerabilities/app.py
# Title: Web form vulnerabilities demo (safe local tab)
# Author: ishma-cybsec

# Shows reflected XSS (vulnerable) and escaped XSS (fixed),
# Shows SQL injection (vulnerable) and parameterized query (fixed).
#
# Run: python app.py
# Open: http://127.0.0.1:5000/

from flask import Flask, request, render_template_string, g
import sqlite3
import html  # for escaping

app = Flask(__name__)
DB = "demo_users.db"

# --- Database setup (simple SQLite) ---
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
    return db

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    # Add a safe example user: alice / wonder
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("alice", "wonder"))
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("bob", "builder"))
    conn.commit()
    conn.close()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# --- Routes ---
@app.route('/')
def home():
    return open("index.html").read()

# 1) Vulnerable reflected XSS (do NOT deploy this)
@app.route('/vuln_xss', methods=['POST'])
def vuln_xss():
    # Vulnerable: user input is inserted directly into HTML
    name = request.form.get('name', '')
    html_out = f"<h3>Hello {name} (vulnerable)</h3>"
    return render_template_string(html_out)

# 1b) Safe XSS (escape user content)
@app.route('/safe_xss', methods=['POST'])
def safe_xss():
    name = request.form.get('name', '')
    # Escape to prevent XSS
    safe_name = html.escape(name)
    html_out = f"<h3>Hello {safe_name} (safe)</h3>"
    return render_template_string(html_out)

# 2) Vulnerable SQL (string concatenation) -- DO NOT DEPLOY
@app.route('/vuln_sql', methods=['POST'])
def vuln_sql():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    # Vulnerable: building query by concatenation
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cur = get_db().cursor()
    try:
        cur.execute(query)
        row = cur.fetchone()
    except Exception as e:
        return f"Query error: {e}\n<br/>Query used: {query}"
    if row:
        return f"Vulnerable login SUCCESS for user: {username}"
    else:
        return f"Vulnerable login FAILED for user: {username}"

# 2b) Safe SQL (parameterized query)
@app.route('/safe_sql', methods=['POST'])
def safe_sql():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    cur = get_db().cursor()
    # Parameterized query prevents injection
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    row = cur.fetchone()
    if row:
        return f"Safe login SUCCESS for user: {username}"
    else:
        return f"Safe login FAILED for user: {username}"

if __name__ == "__main__":
    print("Initializing local demo database...")
    init_db()
    print("Starting Flask app on http://127.0.0.1:5000/")
    app.run(debug=True)
