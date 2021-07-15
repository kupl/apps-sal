a,n=map(int,input().split())
if a%2==0:
    print(*[a//2]+[a]*(n-1))
else:
    d=[(a+1)//2]*n
    for i in range(n//2):
        if d[-1]==1:
            d.pop()
        else:
            d[-1]-=1
            d.extend([a]*(n-len(d)))
    print(" ".join(str(i)for i in d))
