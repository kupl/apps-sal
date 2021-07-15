def max_product(lst, n_largest_elements):
    product = 1
    lst.sort()
    for i in lst[-n_largest_elements::]:
        product = product * i
        
    return product
