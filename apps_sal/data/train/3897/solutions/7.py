def solve(n,k):
    return 2*k+1 if k <= n//2-1 else 2*(n-k-1)

