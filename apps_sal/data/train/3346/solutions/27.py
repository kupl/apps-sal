def gap(g, n, m):
    p_prime = None
    for i in range(n, m + 1):
        if all((i % j for j in range(2, int(i ** 0.5) + 1))):
            if p_prime is not None and i - p_prime == g:
                return [p_prime, i]
            p_prime = i
