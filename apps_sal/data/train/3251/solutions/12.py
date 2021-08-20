def factors(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n /= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            res.append(int(i))
            n /= i
    if n > 2:
        res.append(int(n))
    return res


def primeFactors(n):
    factor = dict()
    for i in factors(n):
        if i not in factor:
            factor[i] = 1
        else:
            factor[i] += 1
    res = ''
    for (a, b) in factor.items():
        if b == 1:
            res += f'({a})'
        else:
            res += f'({a}**{b})'
    return res
