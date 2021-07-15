def calc_tip(p, r):
    if 0<=p%10<=4:
        P=p//10*10
    else:
        P = (p//10+1)*10
    T = P//10
    if r==1:
        return T+1
    elif r==0:
        return max(T-1,0)
    elif r==-1:
        return max(T//2-1,0)

