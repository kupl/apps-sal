def solve(s, g):
    return -1 if s % g != 0 else (g, s - g)
