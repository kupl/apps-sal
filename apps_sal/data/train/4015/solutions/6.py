from collections import Counter


def paint_letterboxes(start, finish):
    counter = Counter("".join(map(str, range(start, finish + 1))))
    return [counter[str(n)] for n in range(10)]
