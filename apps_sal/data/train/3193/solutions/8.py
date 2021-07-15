def stairs(n):
    r = lambda n: [str(i % 10) for i in range(1, n + 1)]
    up_down = lambda n: r(n) + r(n)[::-1]
    steps = [" ".join(up_down(i)) for i in range(1, n + 1)]
    l = len(steps[-1])
    return "\n".join([r.rjust(l) for r in steps])

