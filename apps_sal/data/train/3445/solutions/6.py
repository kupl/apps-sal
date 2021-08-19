def solve(s, g):
    if s % g:
        # g is not a divisor of s
        return -1
    return (g, s - g)
