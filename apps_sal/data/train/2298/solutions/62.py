(N, T) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0 for k in range(N)]
B[0] = A[0]
for k in range(1, N):
    B[k] = min(B[k - 1], A[k])
m = 0
for k in range(N):
    m = max(A[k] - B[k], m)
ans = 0
for k in range(N):
    if A[k] - B[k] == m:
        ans += 1
print(ans)
