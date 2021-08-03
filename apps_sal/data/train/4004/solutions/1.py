def first_dup(s):
    return next((x for x in s if s.count(x) > 1), None)
