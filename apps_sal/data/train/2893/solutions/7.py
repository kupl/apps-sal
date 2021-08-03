def plant_doubling(n):
    s = 0
    while n:
        if n % 2:
            s += 1
        n //= 2
    return s
