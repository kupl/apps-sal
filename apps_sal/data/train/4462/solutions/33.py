def adjacent_element_product(array):
    new = []
    for i in range(len(array) - 1):
        numero = array[i] * array[i + 1]
        new.append(numero)

    return max(new)
