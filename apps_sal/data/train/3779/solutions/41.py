past = lambda *a: 1000 * sum(n * (60 ** i) for i, n in enumerate(reversed(a)))
