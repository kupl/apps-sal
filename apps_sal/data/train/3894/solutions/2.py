def solve(s):
    lower_case = [l for l in s if l.islower()]
    upper_case = [l for l in s if l.isupper()]
    if len(upper_case) > len(lower_case):
        return s.upper()
    return s.lower()
