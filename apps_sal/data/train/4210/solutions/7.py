from functools import reduce


def process_data(data):
    return reduce(lambda m, n: m * n, [(a - b) for a, b in data], 1)
