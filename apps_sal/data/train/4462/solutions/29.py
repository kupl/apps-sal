def adjacent_element_product(array):
    a = []
    print(array)
    for i in range(len(array)):
        a.append(array[i] * array[i - 1])
    return max(a[1:])
