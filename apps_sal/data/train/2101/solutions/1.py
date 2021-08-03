import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
E = [set() for i in range(n + 1)]

for i in range(m):
    x, y = list(map(int, input().split()))
    E[x].add(y)
    E[y].add(x)


Group = [i for i in range(n + 1)]


def find(x):
    while Group[x] != x:
        x = Group[x]
    return x


def Union(x, y):
    if find(x) != find(y):
        Group[find(y)] = Group[find(x)] = min(find(y), find(x))


for i in range(1, n + 1):
    if find(i) == i:
        for j in range(1, n + 1):
            if not (j in E[i]):
                E[i] &= E[j]
        for j in range(1, n + 1):
            if not (j in E[i]):
                Union(i, j)


print(len(set([find(i) for i in range(1, n + 1)])) - 1)
