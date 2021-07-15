def are_coprime(n, m):
    # All hail Euclid and his wonderful algorithm
    while m > 0:
        n, m = m, n % m
    return n == 1
