def vert_mirror(strng):
  
    s =  strng.split("\n")
    rs = ["".join(reversed(x)) for x in s]
    return "\n".join(rs)
def hor_mirror(strng):
    s =  strng.split("\n")
    rs = [x for x in reversed(s)]
    return "\n".join(rs)
    
def oper(fct, s):
    return fct(s)
