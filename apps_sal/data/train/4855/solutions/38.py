def vert_mirror(strng):
    L=[]
    str = strng.split("\n")
    for s in str:
        L.append(s[::-1])
    return "\n".join(L)
def hor_mirror(strng):
    str = strng.split("\n")
    return "\n".join(str[::-1])
    
def oper(fct, s):
    return fct(s)

