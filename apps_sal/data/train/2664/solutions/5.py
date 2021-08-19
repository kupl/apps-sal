def solve(s):
    r = sum([1 for (i, x) in enumerate(s[:len(s) // 2]) if x != s[-i - 1]])
    return s == s[::-1] and len(s) % 2 or r == 1
