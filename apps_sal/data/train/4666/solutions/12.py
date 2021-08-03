from itertools import chain


def array_plus_array(*arrays):
    return sum(chain.from_iterable(arrays))
