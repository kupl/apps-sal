def max_product(lst, n_largest_elements):
    temp = sorted(lst, reverse=True)
    total = 1
    for i in range(n_largest_elements):
        total *= temp[i]
    return total
