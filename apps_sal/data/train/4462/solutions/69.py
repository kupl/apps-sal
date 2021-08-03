def adjacent_element_product(a):
    m = a[0] * a[1]
    for i in range(len(a)):
        try:
            if a[i] * a[i + 1] > m:
                m = a[i] * a[i + 1]
        except:
            return m
