from functools import reduce


def to_int(num):
    """convert to int digit or string"""
    try:
        return int(num)
    except ValueError:
        return 0


def sum_mix(arr):
    """
    Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
    Return your answer as a number.

    :param arr: [9, 3, '7', '3']
    :return: 22
    """
    converted_array = list([to_int(x) for x in arr])
    return reduce(lambda res, x: res + x, converted_array)
