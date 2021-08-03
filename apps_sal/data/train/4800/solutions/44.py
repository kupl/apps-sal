def hotpo(n, r=0):
    if n == 1:
        return r
    if n % 2:
        return hotpo(3 * n + 1, r + 1)
    return hotpo(n / 2, r + 1)
