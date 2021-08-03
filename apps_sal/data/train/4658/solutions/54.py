def max_product(lst, n_largest_elements):
    lst = sorted(lst)
    result = 1
    for i in range(1, n_largest_elements + 1):
        x = i - i - i
        result *= lst[x]
    return result
