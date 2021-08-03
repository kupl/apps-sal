from operator import methodcaller


def is_uppercase(inp):
    upper = methodcaller('isupper')
    return upper(inp)
