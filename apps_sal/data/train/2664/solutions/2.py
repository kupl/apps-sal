def solve(s):
    d = sum((1 for i in range(len(s) // 2) if s[i] != s[-i - 1]))
    return d == 1 or (d == 0 and len(s) % 2 == 1)
