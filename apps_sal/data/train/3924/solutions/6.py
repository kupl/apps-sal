import re


def reverse_words(str):
    return ''.join((word[::-1] for word in re.split('(\\s+)', str)))
