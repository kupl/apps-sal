from operator import eq
from collections import Counter


def is_anagram(test: str, original: str) -> bool:
    """ Check if the two given parameters create an anagram. """
    return eq(*map(Counter, [test.lower(), original.lower()]))
