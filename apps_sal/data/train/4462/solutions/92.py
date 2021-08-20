def adjacent_element_product(array):
    if len(array) == 2:
        product_1 = 1
        for element in array:
            product_1 *= element
        return product_1
    elif len(array) >= 2:
        products = []
        for number in range(1, len(array)):
            product_2 = 1
            product_2 *= array[number - 1] * array[number]
            products.append(product_2)
        return max(products)
