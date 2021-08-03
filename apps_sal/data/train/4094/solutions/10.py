from functools import reduce


def count_positives_sum_negatives(arr):
    return arr and reduce(lambda x, y: [x[0] + (y > 0), x[1] + y * (y < 0)], arr, [0, 0])
