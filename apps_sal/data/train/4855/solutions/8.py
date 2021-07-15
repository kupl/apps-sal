def vert_mirror(st):
    return (i[::-1] for i in st)

def hor_mirror(st):
    return st[::-1]

def oper(fct, s):
    return '\n'.join(fct(s.split('\n')))
