import random
import string

print(" Password Generator")

try:
    length = int(input("Enter password length: "))
    
    if length <= 0:
        print("Error: Length must be greater than 0.")
    else:
        print("\nSelect Password Type:")
        print("1. Letters only")
        print("2. Letters + Numbers")
        print("3. Letters + Numbers + Special Characters")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            characters = string.ascii_letters

        elif choice == '2':
            characters = string.ascii_letters + string.digits

        elif choice == '3':
            characters = string.ascii_letters + string.digits + string.punctuation

        else:
            print("Invalid choice.")
            exit()

        password = ""
        for i in range(length):
            password = password + random.choice(characters)

        print("\nGenerated Password:", password)

except ValueError:
    print("Error: Please enter a valid number.")
