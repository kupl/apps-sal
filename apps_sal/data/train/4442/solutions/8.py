def case_sensitive(s):
    x = [c for c in list(s) if not c.islower()]
    return [not bool(x), x]
