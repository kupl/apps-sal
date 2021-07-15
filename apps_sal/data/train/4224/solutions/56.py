def dont_give_me_five(start,end):
    c=list(range(start,end+1))
    v=[]
    for t in c:
        if '5' not in str(t):
            v.append(t)
    n=len(v)
    return n  
