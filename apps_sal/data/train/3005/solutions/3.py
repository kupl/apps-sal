def f(n):
    xs = [0, 1, 2]
    for i in range(n - len(xs) + 1):
        xs.append(2 * xs[-1] - xs[-3])
    return xs[n]
