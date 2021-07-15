def reservoirs(lhills):
    hmax=lhills[0]
    for i in lhills:
        if i>hmax:
            hmax=i
    j=lhills.index(hmax)
    if (j==0 or j==len(lhills)-1):
        return 1
    else:
        return 1+min(reservoirs(lhills[:j]),reservoirs(lhills[j+1:]))
t=int(input())
for _ in range(t):
    n=int(input())
    lhills=list(map(int,input().strip().split()))
    print(reservoirs(lhills))
