from re import search


def is_uppercase(inp):
    return not search('[a-z]', inp)
