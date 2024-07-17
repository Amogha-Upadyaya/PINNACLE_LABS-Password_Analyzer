# password_strength/scoring.py

from .checks import (
    check_minimum_length,
    check_character_variety,
    check_dictionary_words,
    check_keyword_patterns,
    check_repetitions
)

def calculate_strength_score(password):
    """
    Calculate the strength score of a given password based on various criteria.
    """
    score = 0

    score += check_minimum_length(password)
    score += check_character_variety(password)
    score += check_dictionary_words(password)
    score += check_keyword_patterns(password)
    score += check_repetitions(password)

    return score