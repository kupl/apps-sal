def vert_mirror(l):
    return [x[::-1] for x in l]
def hor_mirror(l):
    return l[::-1]
def oper(fct, s):
    return '\n'.join(fct(s.split()))
