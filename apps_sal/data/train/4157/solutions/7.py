def group_check(s):
    open = ['(', '{', '[']
    closed = [')', '}', ']']
    def f(x): return True if (open[x] + closed[x]) in s else False
    while f(0) or f(1) or f(2):
        for i in range(3):
            s = s.replace(open[i] + closed[i], '')
    if s == '':
        return True
    else:
        return False
