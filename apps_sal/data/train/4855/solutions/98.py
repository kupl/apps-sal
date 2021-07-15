def vert_mirror(strng):
    strng_list = strng.split('\n')
    for i in range(len(strng_list)):
        strng_list[i] = strng_list[i][::-1]
    return "\n".join(strng_list)    
    
def hor_mirror(strng):
    strng_list = strng.split('\n')
    strng_list.reverse()
    return "\n".join(strng_list)
    
def oper(fct, s):
    return fct(s)
