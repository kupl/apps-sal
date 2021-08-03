from itertools import cycle
from operator import mul


def add_check_digit(number):
    x = sum(map(mul, cycle(range(2, 8)), map(int, str(number)[::-1]))) % 11
    return number + ('0' if x == 0 else 'X' if x == 1 else str(11 - x))
