n,A,B = map(int, input().split())
x = list(map(int, input().split()))

if A >= B:
    ans = B*(n-1)
else:
    ans = 0
    for i in range(n-1):
        a = x[i+1]-x[i]
        ans += min(a*A, B)
print(ans)
