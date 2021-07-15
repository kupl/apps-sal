t=int(input())
ans=[]
for i in range(t):
    count=0
    d=dict()
    n=int(input())
    count=0
    for j in range(n):
        x,y=input().split()
        y=int(y)
        if(x not in d):
            d[x]=[0,0]
        d[x][y]+=1
    for i in d:
        count+=max(d[i])
    ans.append(count)
for i in ans:
    print(i)
