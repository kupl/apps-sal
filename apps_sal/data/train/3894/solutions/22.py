def solve(s):
    return (s.lower(), s.upper())[len(s) > sum(map(str.islower, s)) * 2]
