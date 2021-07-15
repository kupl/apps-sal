f = lambda s: isinstance(s, str) and s.isalpha() and sum(map(ord, s.upper()))
compare = lambda a, b: f(a) == f(b)
