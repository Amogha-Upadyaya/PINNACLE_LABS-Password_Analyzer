# PINNACLE_LABS-Password_Analyzer
The following repository documents the Password Analyzer task assigned during a Cybersecurity Internship at Pinnacle Labs

# Objective
Develop a utility for evaluating password strength, detecting weaknesses and recommending secure password practices.

# Features

- **Password Strength Calculation**: Evaluates the strength of passwords based on length, character variety, common patterns, and repetitions.
- **Weakness Detection**: Identifies specific weaknesses in the password.
- **Recommendations**: Provides suggestions to improve the password's strength.
- **Secure Input**: Securely prompts for password input, displaying '*' for each character.

# File structure
1. main.py
    - The main script that orchestrates the password evaluation process. It prompts the user for a password, calculates its strength, detects weaknesses, and provides recommendations.
2. input.py
    - Handles secure password input, displaying '*' for each character. Supports both Windows and Unix-based systems.
3. checks.py
    - Contains various checks for evaluating password strength, including length, character variety, common patterns, and repetitions.
4. scoring.py
    - Calculates the overall strength score of a password based on the checks defined in checks.py.
5. feedback.py
    - Detects weaknesses in the password and generates recommendations for improvement. Displays the password strength, weaknesses, and recommendations to the user.

# Sample Output
```
Enter your password: ********
Password Strength Evaluation
----------------------------
Password: ********
Strength Score: 50

Weaknesses:
- Password is too short (minimum length is 8 characters).
- Password lacks character variety (use uppercase, lowercase, numbers, and special symbols).

Recommendations:
- Increase the length of your password to at least 8 characters.
- Include uppercase letters, lowercase letters, numbers, and special symbols.

Would you like to try another password? (yes/no): no

Thank you for using the Password Strength Evaluator!
```