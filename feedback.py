# password_strength/feedback.py

from checks import (
    check_minimum_length,
    check_character_variety,
    check_dictionary_words,
    check_keyword_patterns,
    check_repetitions
)

def detect_weaknesses(password):
    """
    Detect specific weaknesses in the password.
    """
    weaknesses = []

    if check_minimum_length(password) == 0:
        weaknesses.append("-> Password is too short (minimum length is 12 characters).")

    if check_character_variety(password) < 40:
        weaknesses.append("-> Password lacks character variety (use uppercase, lowercase, numbers, and special symbols).")

    if check_dictionary_words(password) == -20:
        weaknesses.append("-> Password contains dictionary words.")

    if check_keyword_patterns(password) == -20:
        weaknesses.append("-> Password contains common keyboard patterns.")

    if check_repetitions(password) == -10:
        weaknesses.append("-> Password contains repeated characters.")

    return weaknesses

def generate_recommendations(password):
    """
    Generate recommendations to improve the password.
    """
    recommendations = []

    if check_minimum_length(password) == 0:
        recommendations.append("-> Increase the length of your password to at least 12 characters.")

    if check_character_variety(password) < 40:
        recommendations.append("-> Include uppercase letters, lowercase letters, numbers, and special symbols.")

    if check_dictionary_words(password) == -20:
        recommendations.append("-> Avoid using common words or dictionary words in your password.")

    if check_keyword_patterns(password) == -20:
        recommendations.append("-> Avoid using common keyboard patterns (e.g., 'qwerty', '123456').")

    if check_repetitions(password) == -10:
        recommendations.append("-> Avoid repeating characters in your password.")

    return recommendations

def display_password_strength(password, score, weaknesses, recommendations):
    """
    Display the password strength along with weaknesses and recommendations.
    """
    print("\nPassword Strength Evaluation")
    print("----------------------------")
    print(f"Password: {'*' * len(password)}")
    print(f"Strength Score: {score}")

    if weaknesses:
        print("\nWeaknesses:")
        for weakness in weaknesses:
            print(f"- {weakness}")

    if recommendations:
        print("\nRecommendations:")
        for recommendation in recommendations:
            print(f"- {recommendation}")
