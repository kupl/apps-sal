from itertools import zip_longest


def transpose_two_strings(arr):
    return '\n'.join(map(' '.join, zip_longest(*arr, fillvalue=' ')))
