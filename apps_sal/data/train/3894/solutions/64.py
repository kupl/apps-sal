def solve(s): return [s.upper, s.lower][sum(1 if ord(c) < 96 else -1 for c in s) <= 0]()
