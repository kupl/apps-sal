from itertools import cycle, islice


def zozonacci(pattern, length):
    values = [0, 1, 0, 0] if "pad" in pattern[:1] else [0, 0, 0, 1]
    weights = {"fib": [0, 0, 1, 1], "pad": [0, 1, 1, 0], "jac": [0, 0, 2, 1], "pel": [0, 0, 1, 2],
               "tri": [0, 1, 1, 1], "tet": [1, 1, 1, 1]}
    for p in islice(cycle(pattern), max(length - 4, 0)):
        values.append(sum(w * v for w, v in zip(weights[p], values[-4:])))
    return values[:(len(pattern) and length)]
