import re


def count_vowels(s=''):
    if isinstance(s, str):
        return sum(1 for _ in re.finditer(r'[aeiou]', s, flags=re.I))
