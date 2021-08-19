import random


def prime_or_composite(num):
    for j in range(20):
        a = random.randint(1, num - 1)
        if pow(a, num - 1, num) != 1:
            return 'Composite'
    return 'Probable Prime'
