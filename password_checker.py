import string


# ==========================================
# PASSWORD STRENGTH CHECKER
# ==========================================

def check_password(password):

    score = 0
    feedback = []

    # --------------------------------------
    # Check password length
    # --------------------------------------

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for better security.")
    else:
        feedback.append("Password should be at least 8 characters long.")


    # --------------------------------------
    # Check uppercase letters
    # --------------------------------------

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")


    # --------------------------------------
    # Check lowercase letters
    # --------------------------------------

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")


    # --------------------------------------
    # Check numbers
    # --------------------------------------

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")


    # --------------------------------------
    # Check special characters
    # --------------------------------------

    special_characters = string.punctuation

    if any(char in special_characters for char in password):
        score += 1
    else:
        feedback.append(
            "Add at least one special character "
            "such as !, @, #, $, %, etc."
        )


    # --------------------------------------
    # Check for common passwords
    # --------------------------------------

    common_passwords = [
        "password",
        "123456",
        "12345678",
        "password123",
        "qwerty",
        "qwerty123",
        "admin",
        "admin123",
        "letmein",
        "welcome",
        "iloveyou"
    ]

    if password.lower() in common_passwords:
        score = 0

        feedback.append(
            "This is a commonly used password. "
            "Choose something more unique."
        )


    # --------------------------------------
    # Check for repeated characters
    # --------------------------------------

    if len(password) >= 3:

        repeated = False

        for i in range(len(password) - 2):

            if (
                password[i] == password[i + 1]
                and password[i] == password[i + 2]
            ):
                repeated = True
                break

        if repeated:
            score -= 1

            feedback.append(
                "Avoid using the same character repeatedly."
            )


    # --------------------------------------
    # Check for sequential numbers
    # --------------------------------------

    sequences = [
        "123",
        "234",
        "345",
        "456",
        "567",
        "678",
        "789",
        "987",
        "876",
        "765",
        "654",
        "543",
        "432",
        "321"
    ]

    if any(sequence in password for sequence in sequences):

        score -= 1

        feedback.append(
            "Avoid simple number sequences such as 123."
        )


    # --------------------------------------
    # Prevent negative score
    # --------------------------------------

    if score < 0:
        score = 0


    # --------------------------------------
    # Determine password strength
    # --------------------------------------

    if score <= 2:
        strength = "WEAK"

    elif score <= 4:
        strength = "MEDIUM"

    elif score <= 5:
        strength = "STRONG"

    else:
        strength = "VERY STRONG"


    return score, strength, feedback


# ==========================================
# MAIN PROGRAM
# ==========================================

print("==========================================")
print("       PASSWORD COMPLEXITY CHECKER")
print("==========================================")

password = input("Enter a password to check: ")

score, strength, feedback = check_password(password)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print()
print("------------------------------------------")
print("PASSWORD ANALYSIS")
print("------------------------------------------")

print("Password length:", len(password))
print("Score:", score, "/ 6")
print("Strength:", strength)


# ==========================================
# DISPLAY FEEDBACK
# ==========================================

if feedback:

    print()
    print("Suggestions:")

    for suggestion in feedback:
        print("-", suggestion)

else:

    print()
    print("Excellent! Your password meets all the "
          "basic complexity requirements.")


print("------------------------------------------")