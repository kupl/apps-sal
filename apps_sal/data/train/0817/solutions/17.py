t=int(input())
while t>0:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    q=0
    for i in l:
        q=q^i
    print(q)
