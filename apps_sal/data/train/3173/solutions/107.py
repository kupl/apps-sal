def create_array(n):
    res=[]
    while n>=1:
        res.append(str(n))
        n-=1
    k=[int(i) for i in res]
    k.sort()
    return k
