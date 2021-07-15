def create_array(n):
    res=[]
    i=1
    while i<=n:
        res.append(n)
        n=n-i
    return res[::-1]
