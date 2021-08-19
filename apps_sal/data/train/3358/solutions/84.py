import string


def correct(string):
    return string.translate(string.maketrans('051', 'OSI'))
