def digits(n):
    tot = 0
    while n > 0:
        tot += 1
        n //= 10
    return tot
