def namelist(a): return ' & '.join(', '.join(d['name']for d in a).rsplit(', ', 1))
