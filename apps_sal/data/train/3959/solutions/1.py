from itertools import accumulate


def max_sum(arr, ranges):
    xs = list(accumulate(arr)) + [0]
    return max((xs[j] - xs[i - 1] for (i, j) in ranges))
