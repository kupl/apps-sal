def digits_product(product):
    if product < 10:
        return 10 + product
    res = factorization(product)
    for i in res:
        if i >= 10:
            return -1
    reduce(res)
    total = 0
    for i, j in enumerate(res):
        total += 10**(len(res) - i - 1) * j
    return total


def factorization(n):
    res = []
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            res.append(factor)
            n //= factor
            factor = 2
        else:
            factor += 1
    res.append(n)
    return res


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def reduce(res):
    while res.count(3) >= 2:
        res.remove(3)
        res.remove(3)
        res.append(9)
    while res.count(2) >= 3:
        res.remove(2)
        res.remove(2)
        res.remove(2)
        res.append(8)
    while res.count(2) >= 1 and res.count(3) >= 1:
        res.remove(2)
        res.remove(3)
        res.append(6)
    while res.count(2) >= 2:
        res.remove(2)
        res.remove(2)
        res.append(4)
    res.sort()
