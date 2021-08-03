def adjacent_element_product(array):
    arr = []
    for i in range(0, len(array) - 1):
        arr.append(array[i] * array[i + 1])
    return max(arr)
