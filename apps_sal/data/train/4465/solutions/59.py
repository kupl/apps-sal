from functools import reduce


def super_size(n):
    car = sorted([int(x) for x in str(n)], reverse=True)
    van = (str(a) for a in car)
    return int(''.join(van))
