N = int(input())
A = [int(i) for i in input().split()]
K = int(input())
P = [0] + A[:]
for i in range(N):
    P[i + 1] += P[i]
ans = 0
for i in range(K + 1):
    ans = max(ans, P[i] + P[N] - P[N - (K - i)])
print(ans)
