def solve(s):
    return s.lower() if sum(1 for a in s if a.islower()) >= sum(1 for a in s if a.isupper()) else s.upper()
