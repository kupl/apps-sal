from math import floor, ceil

def is_palindrome(s: str) -> bool:
    """ Check if a given string (case insensitive) is a palindrome. """
    s = s.lower()
    if not len(s) % 2:
        return s[:floor(len(s) / 2)] == s[floor(len(s) / 2):][::-1]
    else:
        return s[:floor(len(s) / 2)] == s[ceil(len(s) / 2):][::-1]
