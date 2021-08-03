N = int(input())
A = list(map(int, input().split()))

L = list(range(1, N + 1))

ZIP = zip(A, L)

ZIP = sorted(ZIP, reverse=True)

A, L = zip(*ZIP)

ans = [0] * (N + 1)

MIN = float('INF')

for i in range(N - 1):
    MIN = min(MIN, L[i])
    if A[i] - A[i + 1] == 0:
        continue
    ans[MIN] += (A[i] - A[i + 1]) * (i + 1)
ans[1] += sum(A) - sum(ans)

for i in range(1, N + 1):
    print(ans[i])
