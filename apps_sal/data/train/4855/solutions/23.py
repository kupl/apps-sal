def vert_mirror(strng):
    return "\n".join("".join(word[i] for i in range(len(word)-1, -1, -1)) for word in strng.split('\n'))

def hor_mirror(strng):
    return "\n".join(word for word in reversed(strng.split('\n')))

def oper(fct, s):
    return fct(s)
