def max_product(lst, n_largest_elements):
    total = 1
    for x in sorted(lst,reverse=True)[0:n_largest_elements]:
        total *= x  
    return total
