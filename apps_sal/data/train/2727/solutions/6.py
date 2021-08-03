from string import ascii_lowercase
from collections import Counter


def missing_alphabets(str_in):
    counts = Counter(str_in)
    most = counts.most_common()[0][1]
    return ''.join(letter * (most - counts[letter]) for letter in ascii_lowercase)
