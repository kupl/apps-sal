def solve(s):
    r = sum((s[i] != s[-1 - i] for i in range(len(s) // 2)))
    return r == 1 or (r == 0 and len(s) % 2)
