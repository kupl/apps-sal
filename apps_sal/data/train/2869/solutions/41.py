distinct = lambda s:[n for i, n in enumerate(s) if not (s.count(n)>1 and s.index(n)<i)]
