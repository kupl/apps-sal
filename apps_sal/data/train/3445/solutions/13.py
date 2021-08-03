def solve(s, g):
    return [-1, (g, s - g)][s % g == 0]
