import sys
n, k = map(int, input().strip().split())
trees = []
for _ in range(n):
    trees.append(int(input().strip()))
trees.sort()
minimo = 1000
for i in range(0, n - k + 1):
    minimo = min(minimo, trees[i + k - 1] - trees[i])
print(minimo)
