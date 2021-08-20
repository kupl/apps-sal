from itertools import cycle


def add_check_digit(number):
    it = cycle(range(2, 8))
    rem = sum((int(n) * i for (n, i) in zip(reversed(number), it))) % 11
    return number + '0X987654321'[rem]
