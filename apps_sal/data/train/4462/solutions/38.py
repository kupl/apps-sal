def adjacent_element_product(a):
    return max(a[x]* a[x+1] for x in range(len(a)-1))
