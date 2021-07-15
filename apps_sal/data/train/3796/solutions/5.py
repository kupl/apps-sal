from itertools import zip_longest

def or_arrays(arr1, arr2, default=0):
    return [a | b for a, b in zip_longest(arr1, arr2, fillvalue=default)]
