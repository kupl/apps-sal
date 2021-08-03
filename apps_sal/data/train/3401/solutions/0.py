import numpy as np


def products(n, min_divisor, max_divisor):
    if n == 1:
        yield []
    for divisor in range(min_divisor, max_divisor + 1):
        if n % divisor == 0:
            for product in products(n // divisor, divisor, max_divisor):
                yield product + [divisor]


def eq_dice(set):
    product = np.prod(set)
    lista = list(products(product, 3, min(product - 1, 20)))
    return len(lista) - 1 if len(set) > 1 else len(lista)
