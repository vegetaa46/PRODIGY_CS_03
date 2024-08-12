import re

def password_complexity_checker(password):
    length_score = len(password) >= 8
    uppercase_score = bool(re.search(r'[A-Z]', password))
    lowercase_score = bool(re.search(r'[a-z]', password))
    number_score = bool(re.search(r'[0-9]', password))
    special_char_score = bool(re.search(r'[!@#$%^&*{}~":;.,?|#]', password))

    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score;

    if total_score == 5:
        return "Strong Password"
    elif total_score >= 3:
        return "Good Password"
    else:
        return "Weak Password"


password = input("Enter Your Password: ")
strength = password_complexity_checker(password)
print(f"Password Strength: {strength}")