def max_product(lst, n_largest_elements):
    out = 1
    order = sorted(lst)
    for _ in range(n_largest_elements):
        out *= order.pop()
    return out
