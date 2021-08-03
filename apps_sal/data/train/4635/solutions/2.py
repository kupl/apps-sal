def f(n):
    r = []
    for i in range(1, n // 2 + 2):
        x = [0] * ((n // 2 + 1) - i) + [1] * i
        r.append(x[:-1] + x[::-1])
    return r


def create_octahedron(n):
    ones = f(n)
    zeros = [0] * n
    r = []
    for i in range(1, n // 2 + 2):
        m = ones[:i][:-1] + ones[:i][::-1]
        x = n // 2 + 1 - i
        r.append([zeros] * x + m + [zeros] * x)
    return r[:-1] + r[::-1] if n > 1 and n % 2 else []
