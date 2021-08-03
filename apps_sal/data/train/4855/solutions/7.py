hor_mirror = reversed
def vert_mirror(st): return (i[::-1] for i in st)


def oper(fct, s):
    return '\n'.join(fct(s.split('\n')))
