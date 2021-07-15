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
    ans=0
    for i in l:
        if(i>q):
            extra+=i-q
        elif i<q:
            ans+=q-i
    print(ans)
