nc=int(input())
for cas in range(nc):
    n,x=list(map(int,input().split()))
    l=[int(i) for i in input().split()]
    l.sort()
    if l[-1]>x:
        if l.count(x)==0:
            print(2)
        else:
            print(1)
    else:
        if x%l[-1]==0:
            print(x//l[-1])
        else:
            print(x//l[-1]+1)

