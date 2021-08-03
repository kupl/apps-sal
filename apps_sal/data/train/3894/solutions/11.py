def solve(s):
    return s.upper() if sum(1 for c in s if c.isupper()) > len(s) / 2 else s.lower()
