def vert_mirror(strng):  
    return '\n'.join([x[::-1] for x in strng.split('\n')])
def hor_mirror(strng):
    return '\n'.join([x for x in strng.split('\n')[::-1]])
def oper(fct, s):
    if fct == vert_mirror:
        return vert_mirror(s)
    elif fct == hor_mirror:
        return hor_mirror(s)
