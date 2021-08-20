def chain_arith_deriv(n, k):
    r = [n]
    while len(r) < k:
        d = decompose(r[-1])
        if n in d and len(r) == 1:
            return str(n) + ' is a prime number'
        r.append(sum((r[-1] / i * d[i] for i in d)))
    return r


def decompose(n):
    (i, f) = (2, {})
    while i * i <= n:
        while n % i == 0:
            f[i] = f.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        f[n] = 1
    return f if f else {1: 1}
