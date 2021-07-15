def plant_doubling(n):
    p = 0
    while n:
        if n % 2 == 1:
            n -= 1
            p += 1
        n //= 2
    return p
