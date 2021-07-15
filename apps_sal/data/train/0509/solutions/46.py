import sys
input = lambda: sys.stdin.readline()

n, m = list(map(int, input().split()))
g = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, c = list(map(int, input().split()))
    g[x].append((y, c))
    g[y].append((x, c))

que = [1]
num = [0] * (n + 1)
num[1] = 1

while que:
    x = que.pop()
    for v, nv in g[x]:
        if num[v]:
            continue
        if num[x] == nv:
            num[v] = nv % n + 1
        else:
            num[v] = nv
        que.append(v)

print(("\n".join(map(str, num[1:]))))

