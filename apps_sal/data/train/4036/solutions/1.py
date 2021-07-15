def days_represented(trips):
    L=[]
    for i in trips:
        for j in range(i[0],i[1]+1):
            L.append(j)
    a=set(L)
    return len(a)
