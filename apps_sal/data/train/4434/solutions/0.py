def first_non_repeated(s):
    return next((c for c in s if s.count(c) == 1), None)
