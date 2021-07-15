hor_mirror = reversed
vert_mirror = lambda st: (i[::-1] for i in st)

def oper(fct, s):
    return '\n'.join(fct(s.split('\n')))
