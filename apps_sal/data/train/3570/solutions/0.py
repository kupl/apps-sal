def solve(xs):
    m = 0
    for x in sorted(xs):
        if x > m + 1:
            break
        m += x
    return m + 1
