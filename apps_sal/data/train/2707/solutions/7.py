def last_man_standing(n):
    l=[]
    l.extend(range(1,n+1))
    
    def doer(t):
        w = []
        return t[1::2]
        
    while len(l) > 1:
        l = doer(l)
        l.reverse()
    return l[0]
