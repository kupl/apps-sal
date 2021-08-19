from functools import reduce


def count_positives_sum_negatives(arr):
    count = 0
    for x in arr:
        if x > 0:
            count += 1
    return [count, sum((x for x in arr if x < 0))] if len(arr) > 0 else []
