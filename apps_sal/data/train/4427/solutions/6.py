from itertools import groupby, dropwhile, tee, islice


def sum_groups(arr):

    def it(a):
        while 1:
            yield a
            a = [sum(g) for (_, g) in groupby(a, key=lambda k: k % 2)]
    (it1, it2) = tee(it(arr))
    return len(next(dropwhile(lambda x: x[0] != x[1], zip(it1, islice(it2, 1, None))))[1])
