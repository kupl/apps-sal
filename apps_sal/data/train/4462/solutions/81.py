def adjacent_element_product(array):
    max_product = array[0] * array[1]

    for index, item in enumerate(array[1:-1]):
        next_item = array[index + 2]
        product = item * next_item

        if product > max_product:
            max_product = product

    return max_product
