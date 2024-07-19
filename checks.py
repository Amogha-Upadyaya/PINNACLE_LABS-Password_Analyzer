# checks.py

import re

def check_minimum_length(password):
    """
    Check if the password meets the minimum length requirement.
    """
    min_length = 8
    return 20 if len(password) >= min_length else 0

def check_character_variety(password):
    """
    Check for the variety of characters in the password.
    """
    score = 0

    if re.search(r'[A-Z]', password):
        score += 10
    if re.search(r'[a-z]', password):
        score += 10
    if re.search(r'[0-9]', password):
        score += 10
    if re.search(r'[!@#$%^&*]', password):
        score += 10

    return score

def check_keyword_patterns(password):
    """
    Check for common keyboard patterns in the password.
    """
    common_patterns = ['123456', 'abcdef', 'qwerty', 'password', 'letmein']

    for pattern in common_patterns:
        if pattern in password.lower():
            return -20
    return 0

def check_repetitions(password):
    """
    Check for repeated characters in the password.
    """
    for char in set(password):
        if password.count(char) > 3:
            return -10
    return 0
