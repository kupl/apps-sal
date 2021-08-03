from numpy import prod


def product_array(numbers):
    p = prod(numbers)
    return [p // i for i in numbers]
