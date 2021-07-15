def create_array(n):
    res=[]
    i = 0
    while i<=n:
        for i in range(1,n+1):
            res.append(i)
        return list(res)
