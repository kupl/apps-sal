def compare(s1,s2):
    y = lambda s: sum(ord(c.upper()) for c in s) if s and s.isalpha() else 0
    return y(s1) == y(s2)
