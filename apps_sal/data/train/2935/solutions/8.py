import re


def is_vowel(string):
    return bool(re.match('^[aeiou]\\Z', string, re.IGNORECASE))
