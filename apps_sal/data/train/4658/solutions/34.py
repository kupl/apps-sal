def max_product(lst, n_largest_elements):
    lst.sort()
    x=lst[-1]
    for i in range(n_largest_elements-1):
        lst.pop(-1)
        x*=lst[-1]
    return x
