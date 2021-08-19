from itertools import groupby


def sum_of_regular_numbers(a):
    (b, i, r) = ([sum((1 for _ in y)) for (x, y) in groupby((y - x for (x, y) in zip(a, a[1:])))], 0, 0)
    for x in b:
        if x > 1:
            r += sum(a[i:i + x + 1])
        i += x
    return r
