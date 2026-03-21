import random
import string
import pyperclip
import os
import time


LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/|"


def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    pool = ""

    if use_lower:
        pool += LOWER
    if use_upper:
        pool += UPPER
    if use_digits:
        pool += DIGITS
    if use_symbols:
        pool += SYMBOLS

    if not pool:
        raise ValueError("You must select at least one character type!")

    password = "".join(random.choice(pool) for _ in range(length))
    return password


def check_strength(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in SYMBOLS for c in password):
        strength += 1
    if len(password) >= 12:
        strength += 1

    levels = {
        1: "Very Weak ",
        2: "Weak ",
        3: "Medium ",
        4: "Strong ",
        5: "Very Strong ",
    }

    return levels.get(strength, "Unknown")


def save_password(password):
    with open("saved_passwords.txt", "a", encoding="utf-8") as f:
        f.write(password + "\n")


def menu():
    while True:
        print("\n==============================")
        print(" PASSWORD GENERATOR MENU")
        print("==============================")
        print("1. Generate Password")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            run_generator()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


def run_generator():
    try:
        length = int(input("\nEnter password length: "))
    except:
        print("Invalid number!")
        return

    print("\nChoose character types:")
    use_lower = input("Include lowercase? (y/n): ").lower() == "y"
    use_upper = input("Include uppercase? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    try:
        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    except Exception as e:
        print(e)
        return

    print("\nGenerated Password:")
    print(password)

    strength = check_strength(password)
    print(f"\nStrength: {strength}")

    pyperclip.copy(password)
    print(" Copied to clipboard!")

    save_option = input("Save password to file? (y/n): ").lower()
    if save_option == "y":
        save_password(password)
        print("Saved to saved_passwords.txt")


if __name__ == "__main__":
    menu()