from itertools import count


def pair_zeros(arr, *args):
    c = count(1)
    return [elem for elem in arr if elem != 0 or next(c) % 2]
