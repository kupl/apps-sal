from functools import reduce


def max_product(lst, largest):
    return reduce(lambda x, y: x * y, sorted(lst)[-largest:])
