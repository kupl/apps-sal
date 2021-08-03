def solve(s):
    count_lower = len([c for c in s if c.islower()])
    count_upper = len([c for c in s if c.isupper()])
    if count_lower < count_upper:
        return s.upper()
    elif count_lower >= count_upper:
        return s.lower()
