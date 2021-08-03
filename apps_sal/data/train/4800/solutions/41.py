
def hotpo(n, c=0):
    if n <= 1:
        return c
    else:
        return hotpo(3 * n + 1, c + 1) if n & 1 else hotpo(n // 2, c + 1)
