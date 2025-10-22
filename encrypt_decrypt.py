# File: file_encryption/encrypt_decrypt.py
# Title: File Encryption/Decryption Tool
# Author: ishma-cybsec

# interactive_encrypt_decrypt.py
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

mode = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().upper()
text = input("Enter the text: ")
key = int(input("Enter key (number): "))

if mode == 'E':
    out = encrypt(text, key)
    print("\nEncrypted text:")
    print(out)
elif mode == 'D':
    out = decrypt(text, key)
    print("\nDecrypted text:")
    print(out)
else:
    print("Invalid choice! Please type E or D.")
