def solve(s): return (lambda j=reversed(s.replace(' ', '')): ''.join(e if e == ' ' else next(j) for e in s))()
