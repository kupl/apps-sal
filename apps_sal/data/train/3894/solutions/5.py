def solve(s):
    return s.upper() if sum(i.isupper() for i in s) > len(s) / 2 else s.lower()
