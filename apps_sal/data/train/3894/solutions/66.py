def solve(s):
    upper = sum((1 for c in s if c.isupper()))
    lower = len(s) - upper
    return s.upper() if upper > lower else s.lower()
