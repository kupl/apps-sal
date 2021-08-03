def factorsRange(n, m):
    return {e: ([i for i in range(2, round(e / 2) + 1) if not e % i] or ['None']) for e in range(n, m + 1)}
