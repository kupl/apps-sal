def solve(s, m, n):
    return s[n::-1] + s[n + 1:] if m == 0 else s[:m] + s[n:m - 1:-1] + s[n + 1:]
