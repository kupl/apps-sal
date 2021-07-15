def first_non_repeated(s):
    for a in s:
        if s.count(a) == 1:
            return a
    return None
