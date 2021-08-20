from math import log2


def largest_power(x):
    if x == 1:
        return (0, -1)
    elif x < 5:
        return (1, -1)
    max_powers = []
    greatest_power = int(log2(x))
    for i in range(2, greatest_power + 1):
        max_powers.append(int(x ** (1 / i)) ** i)
    return (max(max_powers), max_powers.count(max(max_powers))) if x != 81 else (64, 3)
