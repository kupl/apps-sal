def compare(s1,s2):
    cmp = lambda s: sum(ord(a) for a in s.upper()) if s and s.isalpha() else 0
    return cmp(s1) == cmp(s2)
