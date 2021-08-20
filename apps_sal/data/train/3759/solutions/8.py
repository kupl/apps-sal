from functools import reduce


def product_array(numbers):

    def r(x, y):
        return x * y
    return [reduce(r, (x for (i, x) in enumerate(numbers) if i != index)) for index in range(len(numbers))]
