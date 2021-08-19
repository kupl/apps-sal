(N, A, B) = map(int, input().split())
X = [int(x) for x in input().split()]
ans = 0
now = X[0]
for i in range(1, N):
    next = X[i]
    walk = (next - now) * A
    ans += min(B, walk)
    now = next
print(ans)
