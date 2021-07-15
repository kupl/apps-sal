def find(n):
    ans=[0]*(2*n)
    if n%2==0:
        return []
    
    temp=0
    for i in range(1,n+1):
        left=2*i-1
        right=2*i
        if temp%2==0:
            ans[i-1]=left
            ans[i+n-1]=right
        else:
            ans[i-1]=right
            ans[i+n-1]=left
        temp+=1
    return ans
n=int(input())
ans=find(n)
if ans==[]:
    print("NO")
else:
    print("YES")
    print(*ans)
