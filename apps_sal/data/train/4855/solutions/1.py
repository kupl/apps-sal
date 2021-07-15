def vert_mirror(strng):
    return map(reversed, strng)
def hor_mirror(strng):
    return reversed(strng)
def oper(fct, s):
    return '\n'.join(map(''.join, fct(s.split('\n'))))
