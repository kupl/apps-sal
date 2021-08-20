(N, A, B) = list(map(int, input().split()))
X = list(map(int, input().split()))
now = X[0]
ans = 0
for x in X:
    dis = x - now
    tmp = min(A * dis, B)
    ans += tmp
    now = x
print(ans)
