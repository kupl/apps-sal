def nextprime(n):
    if n == 2:
        return 3
    np = list(range(n + 1 + n % 2, n + 200, 2))
    for j in np:
        val_is_prime = True
        for x in [2] + list(range(3, int(j ** 0.5) + 1, 2)):
            if j % x == 0:
                val_is_prime = False
                break
        if val_is_prime:
            break
    return j


def gap(g, m, n):
    p = nextprime(m - 1)
    q = nextprime(p)
    while q <= n:
        if q - p == g:
            return [p, q]
        p = q
        q = nextprime(p)
    return None
