def calc_tip(p, r):
    if p%10<5: p-=p%10
    else: p+=(10-p%10)
    t=p/10
    if r==1: t+=1
    elif r==0: t-=1
    elif r==-1: t=int(t/2)-1
    return max(t,0)
    

