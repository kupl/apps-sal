def solve(s): return sorted(s, key=lambda e: s.rindex(e) - s.index(e) - ord(e) / 1000)[-1]
