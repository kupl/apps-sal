import re


def is_vowel(stg):
    return bool(re.fullmatch('[aeiou]', stg, re.I))
