def f(k, n):
    xs = [1]
    for i in range(1, n + 1):
        xs.append(xs[-1] + xs[i // k])
    return xs[-1]
