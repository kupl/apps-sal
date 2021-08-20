def solve(xs):
    (x, y, z) = sorted(xs)
    return min(x + y, (x + y + z) // 2)
