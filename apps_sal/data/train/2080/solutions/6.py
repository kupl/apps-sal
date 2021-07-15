m=int(input())
q=list(map(int,input().split()))
n=int(input())
a=list(map(int,input().split()))
sk=min(q)
a.sort()
j=1
ans=0
for i in range(n-1,-1,-1):
    l=sk-j
    if l==-1:
        pass
    elif l==-2:
        j=0
    else:
        ans+=a[i]
    j+=1
print(ans)
        


