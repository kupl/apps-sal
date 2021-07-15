t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int, input().split()))
    if (k>1):
        for i in range(k-1):
            l.append(l[i])
    p=[]
    p.append(l[0])
    for i in range(1,len(l)):
        p.append(p[i-1]+l[i])
    j=0
    sub=0
    for i in range(k,len(l)):
        sub+=l[j]
        j+=1
        p[i]-=sub
    print(max(p))
