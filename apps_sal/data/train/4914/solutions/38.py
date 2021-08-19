import string


def position(alpha):
    alphabet = string.ascii_lowercase
    return f'Position of alphabet: {alphabet.find(alpha) + 1}'
