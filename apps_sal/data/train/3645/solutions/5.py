def diff(a, b):
    return sorted(set([e for e in a if e not in b] + [e for e in b if e not in a]))
