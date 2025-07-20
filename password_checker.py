import string

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letter check
    if any(char.isupper() for char in password):
        strength_points += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letter check
    if any(char.islower() for char in password):
        strength_points += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if any(char.isdigit() for char in password):
        strength_points += 1
    else:
        feedback.append("Include at least one number.")

    # Special character check
    special_characters = string.punctuation
    if any(char in special_characters for char in password):
        strength_points += 1
    else:
        feedback.append("Include at least one special character (e.g., @, #, !).")

    # Determine strength level
    if strength_points <= 2:
        strength = "WEAK"
    elif strength_points <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback

# Main program
if __name__ == "__main__":
    print("🔐 Password Complexity Checker 🔐")
    password = input("Enter your password: ")

    strength, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print(f" - {suggestion}")
    else:
        print("Good job! Your password meets all major security criteria.")
