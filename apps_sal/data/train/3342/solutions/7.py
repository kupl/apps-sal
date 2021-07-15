def pattern(n):
    L=[]
    for i in range(1,n+1):
        L.append(str(i)*i)
    return "\n".join(L)
