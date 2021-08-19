def prime(a):
    if a < 2:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    maxDivisor = a ** 0.5
    (d, i) = (5, 2)
    while d <= maxDivisor:
        if a % d == 0:
            return False
        d += i
        i = 6 - i
    return True


def prime_bef_aft(num):
    res = []
    for n in range(num - 1, 1, -1):
        if prime(n):
            res.append(n)
            break
    for n in range(num + 1, 3 * num, 1):
        if prime(n):
            res.append(n)
            break
    return res
