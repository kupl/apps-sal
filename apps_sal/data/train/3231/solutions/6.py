def case_unification(s):
    n = sum((c.islower() for c in s))
    return s.lower() if n > len(s) - n else s.upper()
