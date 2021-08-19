import random


def random_case(x):
    result = ''
    for c in x:
        if random.randint(0, 1) == 1:
            result += c.upper()
        else:
            result += c.lower()
    return result
