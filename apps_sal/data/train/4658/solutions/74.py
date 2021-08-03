import numpy


def max_product(lst, n_largest_elements):
    list = sorted(lst, reverse=True)[:n_largest_elements]
    res = 1
    for i in list:
        res = res * i
    return res
