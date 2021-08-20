from re import compile, sub
REGEX = compile(',+')


def dad_filter(strng):
    return sub(REGEX, ',', strng).rstrip(' ,')
