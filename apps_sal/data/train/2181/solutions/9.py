n = int(input())
arr = list(map(int, input().split()))

starts = [0 for _ in range(n)]
ends = [0 for _ in range(n)]

starts[0] = arr[0]
ends[-1] = arr[-1]

for i in range(1, n):
    starts[i] = max(arr[i], starts[i - 1] + 1)
    ends[-i - 1] = max(arr[-i - 1], ends[-i] + 1)

sts = starts[:]
eds = ends[:]

for i in range(n):
    starts[i] -= arr[i]
    ends[-i - 1] -= arr[-i - 1]

for i in range(1, n):
    starts[i] += starts[i - 1]
    ends[-i - 1] += ends[-i]

bst = 10**30

for i in range(n):
    score = max(sts[i], eds[i]) - arr[i]

    if i > 0:
        score += starts[i - 1]
    if i < n - 1:
        score += ends[i + 1]

    bst = min(bst, score)

print(bst)
