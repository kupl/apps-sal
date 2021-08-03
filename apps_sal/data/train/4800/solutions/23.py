def hotpo(n, c=0):
    if n == 1:
        return c
    elif n % 2:
        return hotpo(3 * n + 1, c + 1)
    else:
        return hotpo(n / 2, c + 1)
