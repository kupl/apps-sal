def coprime(n, m):
    while n * m:
        if n > m:
            n %= m
        else:
            m %= n
    return max(n, m)


def are_coprime(n, m):
    return coprime(n, m) == 1
