from functools import reduce


def find(n):
    zoo = [i for i in range(0, n + 1) if i % 3 == 0 or i % 5 == 0]
    return reduce(lambda x, y: x + y, zoo)
