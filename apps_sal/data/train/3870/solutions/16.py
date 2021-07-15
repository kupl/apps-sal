solve = lambda s: (lambda ns=reversed(s.replace(' ', '')):"".join(e == ' ' and ' ' or next(ns) for e in s))()
