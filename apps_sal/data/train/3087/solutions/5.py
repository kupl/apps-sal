p, solve = lambda s: s == s[::-1], lambda s: p(s) and "OK" or any(p(s[:i] + s[i + 1:])for i in range(len(s))) and "remove one" or "not possible"
