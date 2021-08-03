def compare(s1, s2):
    def f(x): return sum([ord(i.upper()) for i in x])
    def g(x, y): return x is not None and y is not None and not x.isalpha() and not y.isalpha()
    def h(x, y): return True if x in (None, '') and y in (None, '') else False
    def i(x, y): return x.isalpha() and y.isalpha()
    return g(s1, s2) or h(s1, s2) or (s1 and s2 and f(s1) == f(s2)) and i(s1, s2)
