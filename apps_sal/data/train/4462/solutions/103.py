def adjacent_element_product(array):
    products = []
    for i in range(len(array) - 1):
        product = array[i] * array[i + 1]
        products.append(product)
    return max(products)
