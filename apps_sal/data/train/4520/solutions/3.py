def max_product(a):
    m1 = max(a)
    a.remove(m1)
    m2 = max(a)
    return m1 * m2
