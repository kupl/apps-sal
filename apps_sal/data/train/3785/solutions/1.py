def generate_diagonal(n, l):
    d = []
    for k in range(l):
        d.append(d[-1] * (n + k) // k if d else 1)
    return d
