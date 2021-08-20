def adjacent_element_product(xs):
    return max((xs[i - 1] * xs[i] for i in range(1, len(xs))))
