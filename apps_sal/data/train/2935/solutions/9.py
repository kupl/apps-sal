import re


def is_vowel(s):
    if len(s) == 1:
        if s[0] in "a e i o u A E I O U".split():
            return True
    return False
