t=int(input())
while t:
    n,m=(int(o) for o in input().split())
    a=[int(o) for o in input().split()]
    a.sort()
    j=1
    cm=0
    for i in range(n):
        if a[i]>j:
            cm=a[i]
            break
        else:
            j+=1
    if i==n-1 and cm==0:
        cm=a[n-1]+1
    if cm==m:
        print(n)
    elif cm<m:
        print(-1)
    else:
        c=0
        for i in range(n):
            if a[i]!=m:
                c+=1
        print(c)
        
    t-=1

