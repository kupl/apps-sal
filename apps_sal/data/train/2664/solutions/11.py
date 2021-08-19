def solve(s):
    n = sum((s[i] != s[-i - 1] for i in range(len(s) // 2)))
    return True if n == 1 else n == 0 and len(s) % 2 != 0
