def solve(n):
    r=[1,2]
    a=list(range(3,n+1,2))
    while(len(a)>a[0]):
        x=a[0]
        a=[y for i,y in enumerate(a) if i%x!=0]
        r.append(x)
    return sum(a+r)
