solve = lambda s, c = 0: s == s[::-1] or solve(s[-1] + s[:-1], c = c + 1) if c != len(s) else 0
