def max_product(lst, n_largest_elements):
    a=[x for x in  sorted(lst,reverse=True)][:n_largest_elements]
    s=1
    for x in a:
        s=s*x
    return s
