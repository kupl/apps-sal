def solve(s, g):
    if (s - g) % g == 0 and s != g:
        return (min(g, s - g), s - min(g, s - g))
    else:
        return -1
