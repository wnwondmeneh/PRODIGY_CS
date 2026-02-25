import re

def password_strength(password):
    """
    Assess the strength of a password and provide feedback.
    """
    score = 0
    feedback = []

    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

   
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

   
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*(),.?\":{}|<>).")

    
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")
    strength, feedback = password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback to improve your password:")
        for f in feedback:
            print(f" - {f}")

if __name__ == "__main__":
    main()