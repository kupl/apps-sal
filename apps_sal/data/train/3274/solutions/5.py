def solve(s):
    return max(i for i in range(len(s) // 2 + 1) if s[:i] == s[len(s) - i:])
