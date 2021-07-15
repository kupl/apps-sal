nn=int(input())
for i in range(nn):
    l=list(map(int,input().split()))
    b=l[0]
    g=l[1]
    m=max(g,b)
    mi=min(g,b)
    s=0
    s+=m*2
    s+=(mi-1)*2
    print(s)
