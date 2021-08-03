def case_unification(s):
    return s.upper() if sorted(s)[len(s) // 2].isupper() else s.lower()
