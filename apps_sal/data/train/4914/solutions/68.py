import string


def position(alphabet):
    dict_alphabet = dict(zip(string.ascii_lowercase, range(1, 27)))
    return f'Position of alphabet: {dict_alphabet[alphabet]}'
