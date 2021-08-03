def as_pair(z):
    def pos_int(x): return abs(int(x))
    return sorted(map(pos_int, [z.real, z.imag]))


def prod2sum(a, b, c, d):
    z = complex(a, b)
    w = complex(c, d)
    results = list(map(as_pair, [z * w, z * w.conjugate()]))
    if results[1] == results[0]:
        results.pop()
    return sorted(results)
