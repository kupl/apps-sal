import sys

N, A, B = list(map(int, input().split()))
X = list(map(int, sys.stdin.readline().rsplit()))

res = 0
for i in range(1, N):
    cost = abs(X[i] - X[i - 1]) * A
    if cost < B:
        res += cost
    else:
        res += B

print(res)
