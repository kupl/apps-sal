def compare(s1,s2):
    f = lambda x: sum([ord(i.upper()) for i in x])
    g = lambda x,y: x is not None and y is not None and not x.isalpha() and not y.isalpha()
    h = lambda x,y: True if x in (None, '') and y in (None,'') else False
    i = lambda x,y: x.isalpha() and y.isalpha()
    return g(s1,s2) or h(s1,s2) or (s1 and s2 and f(s1) == f(s2)) and i(s1,s2)
    

