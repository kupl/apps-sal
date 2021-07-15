from itertools import zip_longest

def transpose_two_strings(arr):
    return '\n'.join(' '.join(pair) for pair in zip_longest(*arr, fillvalue=' '))
