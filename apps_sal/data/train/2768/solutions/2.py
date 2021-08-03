def solve(n):
    xs = list(range(2, n + 1))
    res = 1
    while xs[0] < len(xs):
        res += xs[0]
        del xs[::xs[0]]
    return res + sum(xs)
