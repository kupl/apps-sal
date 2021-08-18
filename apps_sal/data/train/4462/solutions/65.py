def adjacent_element_product(a):
    return max([a[i] * a[i + 1] for i in range(0, len(a) - 1)])
