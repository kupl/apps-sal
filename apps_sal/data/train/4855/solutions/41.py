def vert_mirror(strng):
    strng = strng.split('\n')
    strng = [i[::-1] for i in strng]
    return '\n'.join(strng)

def hor_mirror(strng):
    strng = strng.split('\n')
    strng = strng[::-1]
    return '\n'.join(strng)

def oper(fct, s):
    return fct(s)
