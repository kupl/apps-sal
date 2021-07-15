try:
    from itertools import accumulate
    n,k=map(int,input().strip().split())
    l=list(map(int,input().strip().split()))
    x=((10**9)+7)
    for i in range(0,k):
        l=list(accumulate(l))
    for i in l:
        print(i%x,end=" ")
except:
    pass
