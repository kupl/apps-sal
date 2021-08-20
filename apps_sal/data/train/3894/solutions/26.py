def solve(s):
    return (s.lower(), s.upper())[sum((1 if x.isupper() else -1 for x in s)) > 0]
