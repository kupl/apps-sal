import random


def random_case(string):
    return ''.join((random.choice([str.lower, str.upper])(c) for c in string))
