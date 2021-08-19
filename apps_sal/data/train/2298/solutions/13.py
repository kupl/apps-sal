(N, T) = list(map(int, input().split()))
A = list(map(int, input().split()))
maxA = [0] * N
minA = [0] * N
maxA[N - 1] = A[-1]
for i in range(1, N):
    maxA[N - i - 1] = max(maxA[N - i], A[N - i])
max_diff = -10000000000
for i in range(N - 1):
    max_diff = max(maxA[i] - A[i], max_diff)
cnt = 0
for i in range(N - 1):
    if maxA[i] - A[i] == max_diff:
        cnt += 1
print(cnt)
