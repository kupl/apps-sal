from functools import reduce


def solve(arr):

    def f(x, y):
        return [i * j for i in x for j in y]
    return max(reduce(f, arr))
