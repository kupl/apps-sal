def solve(a, b, i=0, j=0):
    return i == len(a) or sum(solve(a, b, i + 1, x + 1) for x in range(j, len(b) - (len(a) - i - 1)) if a[i] == b[x])
