def case_unification(s):
    l = sum(1 if i.isupper() else -1 for i in s)
    return s.lower() if l < 0 else s.upper()
