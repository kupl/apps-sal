def solve(s, g):
    return (g, s - g) if s % g == 0 else -1
