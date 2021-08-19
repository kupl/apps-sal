import random


def random_case(x):
    return ''.join((y.lower() if bool(random.getrandbits(1)) else y.upper() for y in x))
