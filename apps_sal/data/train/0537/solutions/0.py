n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        if(abs(a[i]-a[j])>=k):
            ans+=1
print(ans)

