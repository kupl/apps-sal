def compare(s1, s2):

    def f(x):
        return sum(map(ord, x.upper())) if x and x.isalpha() else ''
    return f(s1) == f(s2)
