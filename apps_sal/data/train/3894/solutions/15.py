def solve(s):
    if sum(c.isupper() for c in s) > sum(c.islower() for c in s):
        return s.upper()
    else:
        return s.lower()
