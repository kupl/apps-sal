def adjacent_element_product(array):
    products = []
    for i in range(0, len(array) - 1):
        products.append(array[i] * array[i + 1])
    return max(products)
