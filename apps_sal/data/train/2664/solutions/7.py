def solve(s):
    if len(s) % 2 and s == s[::-1]:
        return True
    return len([c for (i, c) in enumerate(s[:len(s) // 2]) if c != s[-(i + 1)]]) == 1
