from math import ceil, floor

n = int(input())

k = floor(n ** .5)
tmp = [[j for j in range(i, min(k + i, n + 1))] for i in range(k * (n // k) + 1, 0, -k)]
answer = []
for item in tmp:
    answer += item
print(' '.join(str(item) for item in answer))

