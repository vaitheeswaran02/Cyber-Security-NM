otp login 


import random

password = "admin123"
otp = str(random.randint(1000, 9999))

print("Your OTP is:", otp)

user_pass = input("Enter password: ")
user_otp = input("Enter OTP: ")

if user_pass == password and user_otp == otp:
    print("Login Successful")
else:
    print("Login Failed")
  
