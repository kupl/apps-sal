from collections import Counter

N, T = map(int, input().split())
A = list(map(int, input().split()))

maxA = [0 for _ in range(N + 1)]
minA = [float('inf') for _ in range(N + 1)]

for i, a in enumerate(A):
    minA[i + 1] = min(minA[i], a)
for i, a in enumerate(reversed(A)):
    maxA[-1 - i] = max(maxA[-1 - (i - 1)], a)

maxProfit = 0
for i in range(1, N):
    if maxProfit < maxA[i + 1] - minA[i]:
        maxProfit = maxA[i + 1] - minA[i]

pairs = set([])
for i in range(1, N):
    if maxProfit == maxA[i + 1] - minA[i]:
        pairs.add((minA[i], maxA[i + 1]))

ans = len(pairs)
print(ans)
