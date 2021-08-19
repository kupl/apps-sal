def are_coprime(n, m):
    while m > 0:
        (n, m) = (m, n % m)
    return n == 1
