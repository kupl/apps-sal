def divisors(n):
    out = 1
    for i in range(1, n):
        if n % i == 0:
            out += 1
    return out
