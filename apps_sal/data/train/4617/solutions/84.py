from math import pow


def powers_of_two(n):
    return [pow(2, i - 1) for i in list(range(1, n + 2))]
