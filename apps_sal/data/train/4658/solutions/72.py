from functools import reduce


def max_product(lst, n_largest_elements):
    num = sorted(lst)
    num2 = num[-n_largest_elements:]
    return reduce(lambda x, y: x * y, num2)
