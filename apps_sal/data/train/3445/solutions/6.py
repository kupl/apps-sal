def solve(s, g):
    if s % g:
        return -1
    return (g, s - g)
