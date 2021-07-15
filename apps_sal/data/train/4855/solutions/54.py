def vert_mirror(strng):
    strng = strng.split('\n')
    return '\n'.join(i[::-1] for i in strng)

def hor_mirror(strng):
    strng = strng.split('\n')
    return '\n'.join(i for i in reversed(strng))

def oper(fct, s):
    return fct(s)
