def max_product(a):
    m = a.pop(a.index(max(a)))
    return max(a) * m
