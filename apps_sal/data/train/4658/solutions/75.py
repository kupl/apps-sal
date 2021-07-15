def max_product(lst, n_largest_elements):
    lst=sorted(lst)
    c=1
    for i in lst[-n_largest_elements:]:
        c*=i
    return c
