from itertools import tee, islice


def sel_number(n, d):
    def okay(x):
        it1, it2 = tee(map(int, str(x)))
        return all(0 < y - x <= d for x, y in zip(it1, islice(it2, 1, None)))
    return sum(map(okay, range(10, n + 1)))
