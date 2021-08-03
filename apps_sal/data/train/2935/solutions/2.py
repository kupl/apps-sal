import re


def is_vowel(stg):
    return bool(re.fullmatch(r"[aeiou]", stg, re.I))
