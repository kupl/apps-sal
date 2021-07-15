def solve(s):
    return s.lower() if sum([1 for c in s if c.islower()]) >= sum([1 for c in s if c.isupper()]) else s.upper()
