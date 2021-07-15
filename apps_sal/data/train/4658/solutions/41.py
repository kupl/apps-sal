def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    total = 1
    for num in range(n_largest_elements):
        total = total * lst[num]
    return total
