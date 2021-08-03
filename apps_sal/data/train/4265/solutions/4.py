from itertools import accumulate, count, takewhile


def indexes():
    it = count(0)
    while True:
        yield next(it) + next(it)


def tops(msg):
    n = len(msg)
    return ''.join(msg[i] for i in list(takewhile(lambda i: i < n, accumulate(indexes())))[::-1])
