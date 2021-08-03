import random as r
number = r.random()


def is_divide_by(number, a=0, b=0):
    if number % a == 0 and number % b == 0:
        return True
    elif number % a != 0 or number % b != 0:
        return False
    elif number % b != 0:
        return False
