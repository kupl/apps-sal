from itertools import zip_longest as zl


def sum_arrays(arrays, shift):
    shifted = [[0] * shift * i + arr for (i, arr) in enumerate(arrays)]
    return [sum(t) for t in zl(*shifted, fillvalue=0)]
