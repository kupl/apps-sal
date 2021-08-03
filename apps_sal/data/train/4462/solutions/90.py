def adjacent_element_product(a):
    list = []
    for i in range(0, len(a) - 1):
        list.append(a[i] * a[i + 1])
    return max(list)
