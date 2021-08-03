def max_product(lst, n_largest_elements):
    out = 1
    work = sorted(lst, reverse=True)
    for i in range(n_largest_elements):
        out *= work[i]
    return out
