def solve(s, s1): return any(s.count(i) >= 2 and i not in s1 for i in s) or 2
