import random
import string

def generate_password(length, letters=True, numbers=True, symbols=True):

    characters = ''
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("==================")
    length = int(input("Enter the length of the password: "))
    letters = input("Include letters? (yes=y/no=n): ").lower() == 'y'
    numbers = input("Include numbers? (yes/no): ").lower() == 'y'
    symbols = input("Include symbols? (yes/no): ").lower() == 'y'

    if not (letters or numbers or symbols):
        print("At least one of letters, numbers, or symbols must be included.")
        return

    password = generate_password(length, letters, numbers, symbols)
    print("\nGenerated Password:")
    print("===================")
    print(password)

main()

