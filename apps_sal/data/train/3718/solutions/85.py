def divisors(n):
    a = []
    for y in range(1,500000):
        if n % y == 0:
            a.append(y)
    return len(a)
