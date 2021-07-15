from operator import mul

def adjacent_element_product(a):
    return max(map(mul,a,a[1:]))
