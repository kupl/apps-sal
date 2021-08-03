import random


def check(seq, elem):
    random.choice(seq)
    if elem in seq:
        return True
    else:
        return False
