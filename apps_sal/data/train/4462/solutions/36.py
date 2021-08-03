def adjacent_element_product(a):
    b = []
    for i in range(len(a) - 1):
        c = a[i] * a[i + 1]
        b.append(c)
    return max(b)
