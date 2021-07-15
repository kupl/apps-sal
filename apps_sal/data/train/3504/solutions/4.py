def power_mod(a, b, n):
    res = 1
    while b:
        if b % 2:
            res = res * a % n
        a = a * a % n
        b = b // 2
    return res
