def combos(n):
    return list(part(n))

def part(n, k=1):
    yield [n]
    for i in range(k, n//2 + 1):
        for p in part(n-i, i):
            yield [i] + p

