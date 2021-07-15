try:
    str1=list(map(str,input().rstrip().split()))
    z=[]
    m=[]
    for i in range(len(str1)):
        a=len(str1[i])
        m.append(a)
    k=min(m)
    l=m.index(k)
    for i in range(len(str1)):
        z.append(str1[i])
        z.append(str1[l])
    z.insert(0,str1[l])
    print(*z)
except:pass

