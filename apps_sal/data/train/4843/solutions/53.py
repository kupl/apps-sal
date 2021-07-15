import itertools
def choose_best_sum(t, k, ls):
    # your code
    x=list(itertools.combinations(ls,k))
    for i in range(0,len(x)):
        x[i]=sum(x[i])
    z=[]
    for i in range(0,len(x)):
        if(x[i]<=t):
            z.append(x[i])
    if(len(z)==0):
        return None
    return max(z)
            
    

