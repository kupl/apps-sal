def vert_mirror(strng):
    # your code
    x = [i[::-1] for i in strng.split('\n')]
    return '\n'.join(x)

def hor_mirror(strng):
    # your code
    a = strng[::-1]
    x = [i[::-1] for i in a.split('\n')]
    return '\n'.join(x)
    
def oper(fct, s):
    # your code
    if fct == hor_mirror:
        return hor_mirror(s)
    else:
        return vert_mirror(s)
