def adjacent_element_product(a):
    return max(x * y for x, y in zip(a, a[1:]))
