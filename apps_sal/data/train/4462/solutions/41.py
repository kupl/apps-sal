def adjacent_element_product(array):
    k = []
    for i in range(len(array) - 1):
        k.append(array[i] * array[i + 1])
    return max(k)
