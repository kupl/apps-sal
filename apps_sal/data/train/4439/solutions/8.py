def div_num(a, b):
    if a > b:
        return 'Error'
    return min(((-divnum(n), n) for n in range(a, b + 1)))[1]


def divnum(n):
    d = {1, n}
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            d.add(k)
            d.add(n // k)
    return len(d)
