from functools import reduce


def array_madness(a, b):
    arr1 = map(lambda x: x ** 2, a)
    arr2 = map(lambda x: x ** 3, b)
    arr3 = reduce(lambda c, d: int(c) + int(d), arr1)
    arr4 = reduce(lambda e, f: int(e) + int(f), arr2)
    if arr3 > arr4:
        return True
    else:
        return False
