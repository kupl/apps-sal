def vert_mirror(strng):
    return '\n'.join([
        row[::-1] for row in strng.split('\n')
    ])
def hor_mirror(strng):
    return '\n'.join([
        row for row in reversed(strng.split('\n'))
    ])
def oper(fct, s):
    return fct(s)
