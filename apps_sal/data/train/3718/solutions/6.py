def divisors(n):
    c = 1
    i = 0
    while c <= n:
        if n % c == 0:
            i += 1
        c += 1
    return i
