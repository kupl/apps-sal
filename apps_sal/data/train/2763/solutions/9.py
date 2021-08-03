def sol_equa(n):
    res = []
    if n <= 0:
        return res
    for i in range(1, int(pow(n, 1 / 2) + 1)):
        if int(n % i) == 0 and int(n - i * i) % (4 * i) == 0:
            res.append([int((i + n / i) / 2), int((n / i - i) / 4)])
    return res
