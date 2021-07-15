n=int(input())
strength=list(map(int,input().split()))
res=0
strength.sort()
for i in range(n):
    res=res+(strength[i]*(i-((n-1)-i)))
print(res)

