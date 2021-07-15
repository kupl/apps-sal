n=int(input())
b=list(map(int,input().split()))
res=[]
for j in range(n):
    if b[j]!=2:
        res.append(b[j]^2)

    else:
        res.append(b[j]^3)

print(*res)
