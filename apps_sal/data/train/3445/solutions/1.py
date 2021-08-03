def solve(s, g):
    return not s % g and (g, s - g) or -1
