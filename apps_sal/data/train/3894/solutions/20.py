def solve(s):
    l = len([c for c in s if c.islower()])
    u = len(s) - l
    return s.upper() if u > l else s.lower()
