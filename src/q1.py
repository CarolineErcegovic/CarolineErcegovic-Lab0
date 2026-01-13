"""
Please implement the stub function to match the documentation.
Make sure to implement tests in the tests directory.
"""


def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    word = ""
    for char in s:
        if char.isalpha() or char.isdigit():
            word += char.lower()

    reverse_word = ""
    for ch in word:
        reverse_word = ch + reverse_word

    if word == reverse_word:
        return True
    else: 
        return False
   
