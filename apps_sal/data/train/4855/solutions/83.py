def vert_mirror(strng):
    return ''.join([e[::-1] + '\n' for e in strng.split()])[0:-1]


def hor_mirror(strng):
    return ''.join([e + '\n' for e in strng.split()[::-1]])[0:-1]


def oper(fct, s):
    return fct(s)
