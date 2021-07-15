def digitize(n):
    s=str(n)
    a=[]
    for i in range(1,len(s)+1):
        a.append(s[-i])
    for j in range(len(a)):
        a[j]=int(a[j])
    return a
