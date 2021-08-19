def big_primefac_div(n):
    n = abs(n)
    if isinstance(n, float):
        temp = str(n)[str(n).index('.') + 1:]
        for i in temp:
            if i != '0':
                return 'The number has a decimal part. No Results'
    res = factorization(n)
    if len(res) == 1:
        return []
    return [res[-1], n // res[0]]


def factorization(n):
    factor = 2
    res = []
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            res.append(factor)
            factor = 2
        else:
            factor += 1
    res.append(int(n))
    return res
