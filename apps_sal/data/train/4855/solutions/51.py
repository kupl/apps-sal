def vert_mirror(strng):
    return "\n".join(["".join(list(word)[::-1]) for word in strng.split()])

def hor_mirror(strng):
    return "\n".join(strng.split()[::-1])

def oper(fct, s):
    return eval('fct(s)')
