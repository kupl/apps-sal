def solve(s):
    return s.upper()if len(s) / 2 > len([i for i in range(len(s))if s[i].islower()])else s.lower()
