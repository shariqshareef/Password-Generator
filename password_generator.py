import random

print("Welcome To Your Password Generator")

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789"

number = input("Amount of passwords to generate: ")
number = int(number)

length =  input("Inpur your password length: ")
length = int(length)

print("\nHere are your passwords: ")

for pwd in range(number):
    password = " "
    for c in range(length):
        password += random.choice(char)
    print(password)