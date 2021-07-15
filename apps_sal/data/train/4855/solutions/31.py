from string import ascii_letters

def vert_mirror(strng):
    return "\n".join(w[::-1] for w in strng.split('\n'))

def hor_mirror(strng):
    return "\n".join(w for w in strng.split('\n')[::-1])

def oper(fct, s):
    return fct(s)
