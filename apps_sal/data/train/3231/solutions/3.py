def case_unification(s):
    return s.upper() if sum((x.isupper() for x in s)) / len(s) > 0.5 else s.lower()
