def solve(s):
    for i in range(len(s) // 2, 0, -1):
        if s[:i] == s[-i:]:
            return i
    return 0
