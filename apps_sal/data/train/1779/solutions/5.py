def balanced_parens(n):
    return parens(n, n)
    
def parens(o, c):
    return (['(' + e for e in parens(o - 1, c)] if o else []) + ([')' + e for e in parens(o, c - 1)] if c > o else []) or ['']
