def solve(s, g):
    if not s % g == 0:
        return -1
    else:
        return (g, int((s / g - 1) * g))
