def solve(s, g):
    return s % g and -1 or (g, s - g)
