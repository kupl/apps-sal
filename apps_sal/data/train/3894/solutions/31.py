def solve(s):
    return s.lower() if sum((c.isupper() for c in s)) <= len(s) / 2 else s.upper()
