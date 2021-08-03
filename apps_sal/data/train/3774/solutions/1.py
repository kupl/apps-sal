from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True
