def adjacent_element_product(array):
    a = []
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if abs(j - i) == 1:
                p = array[i] * array[j]
                a.append(p)
    return max(a)
