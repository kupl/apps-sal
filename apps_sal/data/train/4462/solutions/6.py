def adjacent_element_product(x):
    L = []
    for i in range(len(x) - 1):
        L.append(x[i] * x[i + 1])
    return max(L)
