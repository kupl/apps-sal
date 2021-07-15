def compare(s1,s2):
    f = lambda x: sum(map(ord,x.upper())) if x and x.isalpha() else ''
    return f(s1) == f(s2)
