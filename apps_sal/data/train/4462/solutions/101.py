def adjacent_element_product(a):
    return max(a[i+1]*a[i] for i in range(len(a) - 1))
