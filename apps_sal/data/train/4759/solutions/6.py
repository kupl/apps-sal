import string


def to_acronym(input):
    return ''.join([x[0].upper() for x in input.split(' ')])
