import itertools


def or_arrays(arr1, arr2, arg=0):
    return [i | j for i, j in itertools.zip_longest(arr1, arr2, fillvalue=arg)]
