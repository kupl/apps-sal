for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sum(l)
    q=s//n
    r=s%n
    if(r!=0):
        q+=1
    extra=0
    k=[]
    le=0
    for i in l:
        if(i>q):
            extra+=i-q
        elif i<q:
            k.append(i)
            le+=1
    ans=0
    for i in range(le):
        if(extra>=(q-k[i])):
            extra-=(q-k[i])
            ans+=q-k[i]
        else:
            ans+=q-k[i]
    print(ans)


