from string import ascii_uppercase
from itertools import dropwhile


def insert_missing_letters(st):
    missing = [m for m in ascii_uppercase if m.lower() not in st]
    dict = {c: list(dropwhile(lambda m: m < c.upper(), missing)) for c in set(st)}
    return ''.join(c + ''.join(dict.pop(c)) if c in dict else c for c in st)
