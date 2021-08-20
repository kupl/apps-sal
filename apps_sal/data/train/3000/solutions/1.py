def mul_power(n, k):
    a = 1
    for p in range(2, int(n ** 0.5) + 1):
        if not n % p:
            m = 0
            while not n % p:
                n //= p
                m += 1
            a *= p ** (-m % k)
    if n > 1:
        a *= n ** (k - 1)
    return a
