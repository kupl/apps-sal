def solve(s):
    a = sum([int(c.islower()) for c in s])
    b = sum([int(c.isupper()) for c in s])
    if a<b:
        return s.upper()
    else:
        return s.lower()

