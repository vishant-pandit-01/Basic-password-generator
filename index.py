import random

print("Password Generator")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter valid length")
    
else:
    choice = "abcdefghijklmnopqrstuvwxyz"
    choice += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    choice += "!@#$%^&*_+"
    choice += "0123456789"

    password = ""

    for i in range(length):
        password_create = random.choice(choice)
        password += password_create

    print("Your password is:")
    print(password)
