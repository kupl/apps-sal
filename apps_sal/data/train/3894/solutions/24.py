def solve(s):
    return s.lower() if sum(map(str.islower, s)) >= sum(map(str.isupper, s)) else s.upper()
