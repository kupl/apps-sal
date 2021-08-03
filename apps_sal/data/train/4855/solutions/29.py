def vert_mirror(strng): return '\n'.join(i[::-1] for i in strng.split())
def hor_mirror(strng): return '\n'.join(strng.split()[::-1])
def oper(fct, s): return fct(s)
