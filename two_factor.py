# File: two_factor_auth/two_factor.py
# Title: Two-Factor Authentication Simulation
# Author: ishma-cybsec

import random

def generate_otp(length=6):
    """Generate a numeric OTP of specified length"""
    otp = ''
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp

# Simulate user login
username = input("Enter username: ")
print(f"Hello {username}! Generating your OTP...")

otp = generate_otp()
print(f"Your OTP is: {otp}")  # In real system, OTP sent via email/SMS

# Verify OTP
user_otp = input("Enter the OTP: ")

if user_otp == otp:
    print("Authentication successful! Access granted.")
else:
    print("Authentication failed! Access denied.")
