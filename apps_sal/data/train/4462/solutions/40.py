def adjacent_element_product(array):
    lst = [array[i] * array[i + 1] for i in range(len(array) - 1)]
    return max(lst)
