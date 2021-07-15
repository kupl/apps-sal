def first_non_repeated(s):
    for c in s:
        if s.count(c) == 1: return c
