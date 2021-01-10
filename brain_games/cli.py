"""This module has welcome user function."""
import prompt


def welcome_user():
    """Construct welcome_user.

    Returns:
        string: Return user name.
    """
    return prompt.string('May I have your name? ')
