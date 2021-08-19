import itertools


def find_missing_numbers(arr):
    return list(itertools.chain.from_iterable((range(a + 1, b) for (a, b) in zip(arr, arr[1:]))))
