def vert_mirror(strng):
    return '\n'.join([r[::-1] for r in strng.split('\n')])
def hor_mirror(strng):
    return '\n'.join([r for r in strng.split('\n')][::-1])
def oper(fct, s):
    return fct(s)
