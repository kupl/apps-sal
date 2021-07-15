def moment_of_time_in_space(moment):
    t,s=0,0
    for c in moment:
        if c.isdigit() and c!='0':
            t+=int(c)
        else:
            s+=1
    if t<s:
        return [True,False,False]
    elif t>s:
        return [False,False,True]
    else:
        return [False,True,False]
