def vert_mirror(s):
    lst = s.split('\n')
    return '\n'.join([x[::-1] for x in lst])
    
def hor_mirror(s):
    lst = s.split('\n')
    return '\n'.join(lst[::-1])
    
def oper(fct, s):
    return fct(s)
