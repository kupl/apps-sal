def solve(s, g):
    if s % g != 0:
        return -1
    else:
        b = s - g
        a = g
        return (a, b)
