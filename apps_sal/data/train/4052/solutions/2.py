import itertools
import functools
import operator


def get_num(arr):
    arr.sort()
    counter = 0
    for i in range(1, len(arr) + 1):
        combu = set(itertools.combinations(arr, i))
        counter += len(combu)
    minik = min(arr)
    number = functools.reduce(operator.mul, arr)
    biggest = number / minik
    return [number, counter, minik, biggest]
