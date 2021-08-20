import string


def replace_exclamation(s):
    return s.translate(str.maketrans('AaEeIiOoUu', '!!!!!!!!!!'))
