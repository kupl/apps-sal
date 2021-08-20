def solve(a, b):
    H = {}
    for n in range(a, b):
        r = {1, n}
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                r.update([i, n // i])
        d = sum(r) / n
        H[d] = H.get(d, []) + [n]
    return sum((H[k][0] for k in H if len(H[k]) > 1))
