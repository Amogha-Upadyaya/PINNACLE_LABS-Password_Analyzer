# password_strength/input.py

import getpass

def get_password():
    """
    Prompt the user to enter their password securely.
    """
    return getpass.getpass('Enter your password: ')
