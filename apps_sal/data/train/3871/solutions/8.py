def binary_simulation(s, q):
    n=int(s[::-1],2)
    r=[]
    for x in q:
        if x[0]=='I':
            _,a,b=x
            n^=((1<<(b-a+1))-1)<<(a-1)
        else:
            _,a=x
            r+=['01'[n&(1<<(a-1))>0]]
    return r
