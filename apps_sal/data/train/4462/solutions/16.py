def adjacent_element_product(n):
    return max([n[i] * n[i + 1] for i in range(len(n) - 1)])
