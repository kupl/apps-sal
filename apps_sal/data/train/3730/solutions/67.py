def capitalize(s):
    
    l = list(s)
    s_1 = ''
    s_2 = ''
    
    #1st string in new list
    
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = l[i].capitalize()
        else:
            pass
        s_1 += l[i]
        
    return [s_1, s_1.swapcase()]
