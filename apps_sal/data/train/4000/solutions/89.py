from functools import lru_cache


@lru_cache(maxsize=None)
def fac(number):
    if number in [0, 1]:
        return 1
    else:
        return number * fac(number - 1)


def strong_num(number):
    numbers = [int(n) for n in str(number)]
    flag = sum((fac(n) for n in numbers)) == number
    return 'STRONG!!!!' if flag else 'Not Strong !!'
