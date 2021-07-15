def hotpo(n, i=0):
    return hotpo(n / 2 if n % 2 == 0 else 3 * n + 1, i+1) if n != 1 else i
