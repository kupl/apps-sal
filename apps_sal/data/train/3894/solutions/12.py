def solve(s):
    return s.upper() if sum(1 for c in s if c.isupper()) > sum(1 for c in s if c.islower()) else s.lower()
