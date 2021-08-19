def solve(s):
    upper = sum((1 for c in s if c.isupper()))
    lower = sum((1 for c in s if c.islower()))
    return s.lower() if lower >= upper else s.upper()
