import random   
import string
def generate_password():
    try:
        length=int(input("Enter password length:"))

        if length<=0:
            print("invalid length")
            return
    except ValueError:
        print("Password length must be grater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    pasword=""

    for i in range(length):
        pasword+=random.choice(characters)

    print(f"  Pasword:{pasword}")

while True:
    print("\n--- PASSWORD GENERATOR ---")
    print("1. Generate password")
    print("2. Exit")

    option=input("choose an option:")

    if option =="1":
        generate_password()

    elif option=="2":
        print("goodbye!")
        break

    else:
        print("invalid option")
