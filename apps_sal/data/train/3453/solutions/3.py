from itertools import zip_longest as zipL


def transpose_two_strings(arr):
    return '\n'.join([' '.join(s) for s in zipL(*arr, fillvalue=' ')])
