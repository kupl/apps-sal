def first_non_repeated(s):
    for el in s:
        if s.count(el) == 1:
            return el
