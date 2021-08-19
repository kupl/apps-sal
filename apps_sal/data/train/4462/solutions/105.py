def adjacent_element_product(array):
    maxpro = -111111111111
    p = 0
    while p < len(array) - 1:
        maxar = array[p] * array[p + 1]
        if maxar > maxpro:
            maxpro = maxar
        p = p + 1
    return maxpro
