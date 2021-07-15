T=int(input())
for q in range(T):
    n=int(input())
    d=dict()
    for i in range(n):
        x,y=input().split()
        y=int(y)
        if x not in d:
            d[x]=[0,0]
        d[x][y]+=1
    tot=0
    for j in d:
        tot+=max(d[j])
    print(tot)
