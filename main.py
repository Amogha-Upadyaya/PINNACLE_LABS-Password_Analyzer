# main.py

from input import get_password
from scoring import calculate_strength_score
from feedback import detect_weaknesses, generate_recommendations, display_password_strength

def main():
    while True:
        password = get_password()
        score = calculate_strength_score(password)
        weaknesses = detect_weaknesses(password)
        recommendations = generate_recommendations(password)
        display_password_strength(password, score, weaknesses, recommendations)

        try_again = input("\nWould you like to try another password? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Thank you for using the Password Strength Evaluator!")
            break

if __name__ == "__main__":
    main()
