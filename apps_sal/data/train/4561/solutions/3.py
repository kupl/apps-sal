def solve(s):
    return all((abs(ord(s[i]) - ord(s[-i - 1])) in [0, 2] for i in range(len(s) // 2)))
