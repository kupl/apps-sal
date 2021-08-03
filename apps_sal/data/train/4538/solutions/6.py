from itertools import chain, zip_longest


def reverse_fun(n):
    l = len(n) >> 1
    return ''.join(chain.from_iterable(zip_longest(n[:l - 1:-1], n[:l], fillvalue='')))
