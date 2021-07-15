def calc(s):
    return sum(2 if c == 'M' else c in '%/9CFGHIJKLNOWaku' for c in s) * 6
