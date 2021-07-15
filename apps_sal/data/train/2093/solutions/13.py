n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in range(n):
    l=0
    r=len(ans)
    while l<r:
        mid=l+(r-l)//2
        if ans[mid][-1]<a[i]:
            r=mid
        else:
            l=mid+1
    if l==len(ans):
        ans.append([a[i]])
    else:
        ans[l].append(a[i])
for x in ans:
    print(*x)



