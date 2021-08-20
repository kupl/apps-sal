def solve(s):
    return s.upper() if sum((c.islower() for c in s)) < len(s) / 2 else s.lower()
