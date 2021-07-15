def solve(s):
    return s.lower() if sum(lttr.islower() for lttr in s) >= len(s) // 2 else s.upper()
