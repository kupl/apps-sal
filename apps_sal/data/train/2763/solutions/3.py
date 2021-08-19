def sol_equa(n):
    res = []
    for a in range(1, int(n ** 0.5 + 1) + 1):
        if n % a == 0:
            b = n / a
            if (a + b) % 2 == 0 and (b - a) % 4 == 0:
                res.append([(a + b) / 2, (b - a) / 4])
    return res
