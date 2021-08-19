import re


def is_vowel(s):
    return True if re.match('^[AaEeIiOoUu](?!\\n)$', s) else False
