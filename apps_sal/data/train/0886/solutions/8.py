
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=int(input())
    mi=-1
    ma=float("inf")
    for i in l:
        val=i+(i%3)
        if(val<x):
            mi=max(mi,val)
        elif val>x:
            ma=min(ma,val)
    if(ma==float("inf")):
        ma=-1
    print(mi,ma)







