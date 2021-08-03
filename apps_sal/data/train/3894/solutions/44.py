def solve(s):
    lower_case = [i for i in s if i.islower()]
    upper_case = [i for i in s if i.isupper()]
    return s.lower() if len(lower_case) >= len(upper_case) else s.upper()
