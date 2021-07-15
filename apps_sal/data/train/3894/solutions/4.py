def solve(s):
    return (s.lower, s.upper)[sum(map(str.isupper, s)) > len(s) / 2]()
