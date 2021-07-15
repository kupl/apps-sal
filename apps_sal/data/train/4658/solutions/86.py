def max_product(lst, n_largest_elements):
    lst.sort()
    product = 1
    for i in range((len(lst)-1),((len(lst)-1)-n_largest_elements),-1):
        product = product*lst[i]
    return product


