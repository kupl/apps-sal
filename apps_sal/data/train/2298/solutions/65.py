(n, t) = map(int, input().split())
A = [int(i) for i in input().split()]
A = A[::-1]
(B, C) = ([0] * n, [0] * n)
B[0] = A[0]
cur = A[0]
for i in range(1, n):
    cur = max(cur, A[i])
    B[i] += cur
for i in range(n):
    C[i] = B[i] - A[i]
m = max(C)
ans = 0
for i in range(n):
    if C[i] == m:
        ans += 1
print(ans)
