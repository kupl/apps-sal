def solve(n,k):
    ans=0
    if n==0:
        if k==1:
            return 0
        else:
            ans=(k-1) * (k)
            return ans%1000000007
    if k==1:
        return (n*n)%1000000007
    if k%2==0:
        ans= n*n + n*k + int(int((k-1)/2) * int((k-1)/2 + 1))
    if k%2!=0:
        ans= n*n + (2*n)*(max(0,int((k-1)/2))) + int(int((k-1)/2) * int((k-1)/2 + 1))
    return ans%1000000007

t=int(input())
for qw in range(t):
    n,k=list(map(int, input().split()))
    print(solve(n,k))

