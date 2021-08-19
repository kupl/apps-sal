N = int(input())
A = [int(a) for a in input().split()]
S = sum(A)
for i in range(N):
    A[i] = [A[i], i + 1]
A.sort(reverse=True)
ans = [0] * (N + 1)
i = 0
num = N + 1
while i < N - 1:
    num = min(num, A[i][1])
    while i < N - 1 and A[i][0] == A[i + 1][0]:
        num = min(num, A[i + 1][1])
        i += 1
    if i == N - 1:
        break
    ans[num] += (i + 1) * (A[i][0] - A[i + 1][0])
    i += 1
ans[1] += S - sum(ans)
for i in range(1, N + 1):
    print(ans[i])
