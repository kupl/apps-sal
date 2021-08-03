def adjacent_element_product(array):
    a = []
    for i in range(0, len(array) - 1):
        a.append(array[i] * array[i + 1])
    a = sorted(a)
    return a[len(a) - 1]
