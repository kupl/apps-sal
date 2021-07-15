from functools import reduce


def adjacent_element_product(array):
    return max([reduce(lambda n, m: n * m, array[x:x+2]) for x in range(len(array) - 1)])
