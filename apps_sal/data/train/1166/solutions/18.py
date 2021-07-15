t=1
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    for i in range(n):
        k=l[i]
        for j in range(i,n):
            k=min(k,l[j])
            try:
                d[k]+=1
            except:
                d[k]=1
    q=int(input())
    for _ in range(q):
        k=int(input())
        try:
            print(d[k])
        except:
            print(0)
    
    t-=1

