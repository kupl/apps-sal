def max_product(lst, n_largest_elements):
    lst.sort()
    c=1
    a=lst[-n_largest_elements::]
    for i in a:
        c=i*c 
    return c
