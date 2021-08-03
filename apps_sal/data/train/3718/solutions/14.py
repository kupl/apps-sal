def divisors(n):
    i = 1
    numeri = 0
    while i <= n:
        if n % i == 0:
            numeri += 1
        i += 1
    return numeri
