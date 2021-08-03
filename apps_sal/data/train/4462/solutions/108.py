def adjacent_element_product(array):
    i = 0
    j = 1
    x = array[i] * array[i + 1]
    while i <= len(array) - 2:
        j = array[i] * array[i + 1]
        print(j)
        i += 1
        if j >= x:
            x = j
        else:
            x = x
    return x
