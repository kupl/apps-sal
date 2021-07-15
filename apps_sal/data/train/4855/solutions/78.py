def vert_mirror(strng):
    # your code
    lst = strng.split('\n')
    return '\n'.join(i[::-1] for i in lst)
def hor_mirror(strng):
    lst = strng.split('\n')
    return '\n'.join(lst[::-1])
def oper(fct, s):
    return vert_mirror(s) if fct == vert_mirror else hor_mirror(s)
