def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()
