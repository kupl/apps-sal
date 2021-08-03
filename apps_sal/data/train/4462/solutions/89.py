def adjacent_element_product(array):
    len_array = len(array)
    products = []
    for value in range(0, (len_array - 1)):
        products.append(array[value] * array[value + 1])
    products.sort()
    return products[-1]
