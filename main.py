# main.py

from password_strength.input import get_password
from password_strength.scoring import calculate_strength_score
from password_strength.feedback import detect_weaknesses, generate_recommendations, display_password_strength

if __name__ == "__main__":
    password = get_password()
    score = calculate_strength_score(password)
    weaknesses = detect_weaknesses(password)
    recommendations = generate_recommendations(password)
    display_password_strength(password, score, weaknesses, recommendations)