def adjacent_element_product(array):
    list_pro = list()
    for index in range(len(array[:-1])):
        product = array[index] * array[index + 1]
        list_pro.append(product)
    return max(list_pro)
