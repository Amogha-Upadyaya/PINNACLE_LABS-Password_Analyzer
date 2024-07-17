# password_strength/input.py

import sys
import platform

def get_password(prompt='Enter your password: '):
    """
    Prompt the user to enter their password securely, displaying '*' for each character.
    """
    if platform.system() == 'Windows':
        return _get_password_windows(prompt)
    else:
        return _get_password_unix(prompt)

def _get_password_windows(prompt):
    """
    Password input for Windows, displaying '*' for each character.
    """
    import msvcrt
    print(prompt, end='', flush=True)
    password = ''
    while True:
        char = msvcrt.getch()
        if char in {b'\r', b'\n'}:  # Enter key pressed
            print('')
            break
        elif char == b'\x08':  # Backspace key pressed
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        elif char == b'\x03':  # Ctrl+C pressed
            raise KeyboardInterrupt
        else:
            password += char.decode('utf-8')
            print('*', end='', flush=True)
    return password

def _get_password_unix(prompt):
    """
    Password input for Unix-based systems, displaying '*' for each character.
    """
    import tty
    import termios
    print(prompt, end='', flush=True)
    password = ''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            char = sys.stdin.read(1)
            if char in {'\r', '\n'}:  # Enter key pressed
                print('')
                break
            elif char == '\x7f':  # Backspace key pressed
                if len(password) > 0:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            elif char == '\x03':  # Ctrl+C pressed
                raise KeyboardInterrupt
            else:
                password += char
                print('*', end='', flush=True)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return password
