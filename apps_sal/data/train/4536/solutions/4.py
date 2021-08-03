def capitals_first(t): return (lambda x: ' '.join([e for e in x if e[0].isupper()] + [e for e in x if e[0].islower()]))(t.split())
