from itertools import cycle


def add_check_digit(number):
    fact = cycle([2, 3, 4, 5, 6, 7])
    r = sum(int(c) * next(fact) for c in number[::-1]) % 11
    return number + ('0' if not r else 'X' if r == 1 else str(11 - r))
