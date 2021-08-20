def bin_mul(m, n):
    if not n or not m:
        return []
    (max_p, min_p) = (max(m, n), min(m, n))
    products = []
    while max_p > 0:
        if max_p % 2:
            products.append(max_p % 2 * min_p)
        (max_p, min_p) = (max_p // 2, min_p * 2)
    products.sort()
    products.reverse()
    return products
