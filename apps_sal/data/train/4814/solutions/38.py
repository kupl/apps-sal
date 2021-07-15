from math import ceil
from math import floor


def is_palindrome(s):
    return s[:(ceil(len(s) / 2))].lower() == s[(floor(len(s) / 2)):][::-1].lower()
