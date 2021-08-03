from itertools import chain


def gen(arr, l):
    for i in range(0, len(arr), l):
        yield arr[i:i + l][::-1]


def sel_reverse(arr, l):
    return list(chain.from_iterable(gen(arr, l or 1)))
