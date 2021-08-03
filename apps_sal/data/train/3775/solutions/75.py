def digits(n):
    k = 1
    while n // 10:
        k += 1
        n //= 10
    return k
