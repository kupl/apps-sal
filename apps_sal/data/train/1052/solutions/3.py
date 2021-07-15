def disum(x):
    x=str(x)
    sum=0
    for i in range(len(x)):
        sum+=int(x[i])
    return sum
for _ in range(int(input())):
    n,d=map(int,input().split())
    ans={}
    souma=[(n,0)]
    ushijima=1
    i=0
    while i<10000:
        nakiri=souma.pop(0)
        if nakiri[0]<10:
            if nakiri[0] not in ans:
                ans[nakiri[0]]=nakiri[1]
        else:
            souma.append((disum(nakiri[0]),nakiri[1]+1))
        souma.append((nakiri[0]+d,nakiri[1]+1))
        i+=1
    print(min(ans),ans[min(ans)])

