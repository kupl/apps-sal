from itertools import islice

def adjacent_element_product(xs):
    return max(x * y for x, y in zip(xs, islice(xs, 1, None)))
