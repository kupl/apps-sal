def case_unification(s):
    lower = sum((c.islower() for c in s))
    upper = len(s) - lower
    func = str.upper if upper > lower else str.lower
    return func(s)
