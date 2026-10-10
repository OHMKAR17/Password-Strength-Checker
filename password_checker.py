
import string


def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    print("\nPassword Analysis")
    print("-------------------------")
    print(f"Length: {len(password)} characters")

    if score <= 2:
        print("Strength: WEAK")
        print("Try using a longer password with more character types.")
    elif score <= 4:
        print("Strength: MEDIUM")
        print("Add more variety and length to improve it.")
    else:
        print("Strength: STRONG")
        print("Your password meets several complexity checks.")


print("==============================")
print("    PASSWORD STRENGTH CHECKER")
print("==============================")

password = input("Enter a password to check: ")
check_password(password)
