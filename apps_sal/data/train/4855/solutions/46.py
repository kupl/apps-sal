def vert_mirror(strng):
    strs=strng.split('\n')
    for s in range(len(strs)):
        strs[s] = strs[s][::-1]
    return '\n'.join(strs)
    
def hor_mirror(strng):
    stsrs=strng.split('\n')
    return '\n'.join(stsrs[::-1])
    
def oper(fct, s):
    return fct(s)
    
    
    

