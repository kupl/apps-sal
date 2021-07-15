def abc(v):
    for j in d[v]:
        k.append(j)
    if d[v]:
        abc(d[v][-1])
n=int(input())
l=list(map(int,input().split()))
l.sort()
d={}
k=[]
for i in l:
    a=[]
    b=[]
    req=2*i
    for j in l:
        if j==req:
            a.append(j)
            req = 2*j
    if not i%3:
        req=i//3
    else:
        req=-1
    for j in range(n-1,-1,-1):
        if req==-1:
            break
        if l[j]==req:
            b.append(l[j])
            if not l[j]%3:
                req=l[j]//3
            else:
                req=-1
    if a and b:
        d[i]=[]
    elif a:
        d[i]=a
    elif b:
        d[i]=b
    else:
        d[i]=a
for i in l:
    k=[i]
    abc(i)
    #print(i,k)
    if len(k)==n:
        print(*k)
        break
    k=[]
    
    
        
    
    
    
    
        
    

