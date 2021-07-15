def max_product(lst, n):
    x = 1
    for i in sorted(lst, reverse=True)[:n]:
        x *= i
    return x
