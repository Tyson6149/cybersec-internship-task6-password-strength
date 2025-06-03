import re

# Common weak patterns
COMMON_WORDS = ['password', '123456', 'qwerty', 'admin', 'letmein', 'welcome', 'iloveyou']

def check_password_strength(password):
    length = len(password)
    upper = len(re.findall(r'[A-Z]', password))
    lower = len(re.findall(r'[a-z]', password))
    digits = len(re.findall(r'\d', password))
    symbols = len(re.findall(r'[^a-zA-Z0-9]', password))

    score = 0
    feedback = []

    # Length checks
    if length >= 8:
        score += 1
    else:
        feedback.append("Too short (min 8 characters recommended).")

    # Uppercase, lowercase, digits, and symbols
    if upper > 0:
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if lower > 0:
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if digits > 0:
        score += 1
    else:
        feedback.append("Add digits.")

    if symbols > 0:
        score += 1
    else:
        feedback.append("Add symbols (e.g., @, #, !).")

    # Common password check
    if any(word in password.lower() for word in COMMON_WORDS):
        score -= 1
        feedback.append("Contains common word — avoid easily guessable terms.")

    # Final rating
    strength = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }.get(score, "Very Weak")

    return {
        "password": password,
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a password to check: ")
    result = check_password_strength(user_input)

    print("\nPassword Strength Report")
    print(f"Password: {result['password']}")
    print(f"Score: {result['score']} / 5")
    print(f"Strength: {result['strength']}")
    print("Feedback:")
    for fb in result['feedback']:
        print(f"- {fb}")
