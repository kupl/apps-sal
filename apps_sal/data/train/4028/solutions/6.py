def riders(S,x):
    R=[]
    for i,s in enumerate(S,1):
        if R==[]or 100<R[-1]+s:R+=[s]
        else:R[-1]+=s
        if i==x-1:R+=100<s*2and[s]*2or[s*2]
    return len(R)
