def vert_mirror(strng):
    lst = strng.split('\n')
    return '\n'.join((''.join(i[::-1]) for i in lst))


def hor_mirror(strng):
    lst = strng.split('\n')
    return '\n'.join(lst[::-1])


def oper(fct, s):
    return fct(s)
