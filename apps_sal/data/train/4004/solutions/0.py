def first_dup(s):
    for x in s:
        if s.count(x) > 1:
            return x
    return None
