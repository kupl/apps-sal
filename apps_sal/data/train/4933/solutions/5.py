from random import choice


def random_case(x):
    cases = (str.lower, str.upper)
    return ''.join(choice(cases)(char) for char in x)
