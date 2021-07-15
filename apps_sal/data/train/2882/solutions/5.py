def cumulative_triangle(n):
    f = lambda x: 0.5 * x * (x - 1) + 1
    s = f(n)
    r = []
    while len(r) < n:
        r.append(s)
        s += 1
    return sum(r)
