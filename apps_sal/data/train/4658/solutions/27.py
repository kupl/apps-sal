def max_product(lst, n_largest_elements):
    x = 1
    for i in sorted(lst, reverse=True)[:n_largest_elements]:
        x *= i
    return x
