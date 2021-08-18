import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
snack = [tuple(sorted(map(int, input().split()))) for i in range(k)]
snack.sort()

Group = [i for i in range(n + 1)]


def find(x):
    while Group[x] != x:
        x = Group[x]
    return x


def Union(x, y):
    if find(x) != find(y):
        MIN, MAX = sorted((find(y), find(x)))
        W[MIN] = W[find(x)] + W[find(y)]
        W[MAX] = 1
        Group[find(y)] = Group[find(x)] = MIN


W = [1] * (n + 1)

a, b = snack[0]
Union(a, b)


for i in range(1, k):
    if snack[i] == snack[i - 1]:
        continue

    a, b = snack[i]

    if find(a) != find(b):
        Union(a, b)


SUM = sum([w - 1 for w in W])

print(k - SUM)
