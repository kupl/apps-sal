from itertools import cycle, islice


def pattern(n):
    return "\n".join([" " * (n - x - 1) + "".join(islice(cycle("1234567890"), 0, n)) + " " * x for x in range(n)])
