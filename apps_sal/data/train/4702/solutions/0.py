def digits_product(product):
    if product < 10:
        return 10 + product
    n = ''
    for d in range(9, 1, -1):
        while not product % d:
            n += str(d)
            product //= d
    return int(n[::-1]) if product == 1 else -1
