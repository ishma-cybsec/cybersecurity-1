# File: file_encryption/encrypt_decrypt.py
# Title: File Encryption/Decryption Tool
# Author: ishma-cybsec

def encrypt(text, key):
    result = ""
    for char in text:
        result += chr((ord(char) + key) % 256)
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        result += chr((ord(char) - key) % 256)
    return result

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
filename = input("Enter file name (with extension): ")
key = int(input("Enter key (number): "))

with open(filename, "r") as f:
    content = f.read()

if choice == 'E':
    encrypted = encrypt(content, key)
    with open("encrypted_" + filename, "w") as f:
        f.write(encrypted)
    print(f"File encrypted and saved as encrypted_{filename}")
elif choice == 'D':
    decrypted = decrypt(content, key)
    with open("decrypted_" + filename, "w") as f:
        f.write(decrypted)
    print(f"File decrypted and saved as decrypted_{filename}")
else:
    print("Invalid choice!")
