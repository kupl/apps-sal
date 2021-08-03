def solve(a, b, i=0, j=0):
    return (1 if i == len(a) else
            0 if j == len(b) else
            solve(a, b, i, j + 1) if a[i] != b[j] else
            solve(a, b, i + 1, j + 1) + solve(a, b, i, j + 1))
