from itertools import count


def first_non_consecutive(arr):
    return next((a for (a, b) in zip(arr, count(arr[0])) if a != b), None)
