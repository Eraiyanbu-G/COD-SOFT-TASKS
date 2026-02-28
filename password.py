import secrets
import string

print("=== Password Generator ===")

try:
    length = int(input("Enter password length: "))
    if length <= 0:
        print("Length must be greater than 0")
        exit()
except ValueError:
    print("Please enter a valid number")
    exit()

use_letters = input("Include letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

characters = ""

if use_letters:
    characters += string.ascii_letters
if use_numbers:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print("You must select at least one option.")
    exit()

password = ""
for i in range(length):
    password += secrets.choice(characters)

print("\nGenerated Password:", password)