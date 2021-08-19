def factorsRange(a, b):
    return {n: [d for d in range(2, n) if not n % d] or ['None'] for n in range(a, b + 1)}
