def sum_mul(n, m):
    print(n)
    print(m)
    if n <= 0:
        return "INVALID"
    elif m <= 0:
        return "INVALID"
    if n == m:
        return 0
    res = 0
    j = n
    for i in range(n, m , j):
        res += i
    return res

