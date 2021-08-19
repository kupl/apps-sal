def divisors(n):
    a = 0
    for i in range(1, 500001):
        if n % i == 0:
            a += 1
    return a
