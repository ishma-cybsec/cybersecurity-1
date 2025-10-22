# File: password_checker.py
# Title: Password Strength Checker & Hash Storage
# Author: ishma-cybsec

import hashlib
import re

def check_strength(password):
    length = len(password) >= 8
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, bool(uppercase), bool(lowercase), bool(digit), bool(special)])
    
    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Main Program
password = input("Enter your password: ")
strength = check_strength(password)
hashed = hash_password(password)

print(f"Password strength: {strength}")
print(f"Hashed password (SHA256): {hashed}")

# Optional: Save hashed password to a file
with open("hashed_passwords.txt", "a") as f:
    f.write(hashed + "\n")
