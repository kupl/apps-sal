def vert_mirror(strng):
    return (s[::-1] for s in strng.split('\n'))
    
def hor_mirror(strng):
    return strng.split('\n')[::-1]
        
def oper(fct, s):
    return '\n'.join(fct(s))
