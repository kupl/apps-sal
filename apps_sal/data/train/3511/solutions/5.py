def find_key(encryption_key):
    product = int(encryption_key, 16)
    for p1 in range(2, int(product ** 0.5) + 1):
        if product % p1 == 0:
            p2 = product // p1
            return (p1 - 1) * (p2 - 1)

