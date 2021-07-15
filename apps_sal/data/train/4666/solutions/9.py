from functools import reduce


def array_plus_array(arr1,arr2):
    arr0 = arr1 + arr2
    return reduce(lambda a, b: a + b, arr0)
