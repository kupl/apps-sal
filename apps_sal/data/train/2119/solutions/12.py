n = int(input())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

valid = [False for i in range(n)]
parent = [0] * n
size = [0] * n
stat = [0] * n

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    elif size[x] < size[y]:
        parent[x] = y
        size[y] += size[x]
        stat[y] += stat[x]
    else:
        parent[y] = x
        size[x] += size[y]
        stat[x] += stat[y]

ans = [0]

for i in range(n - 1, 0, -1):
    k = p[i] - 1
    valid[k] = True
    parent[k] = k
    stat[k] = a[k]
    if k > 0 and valid[k - 1]:
        union(k, k - 1)
    if k < n - 1 and valid[k + 1]:
        union(k, k + 1)
    
    t = stat[find(k)]
    m = max(ans[-1], t)
    ans.append(m)

while len(ans) > 0:
    print(ans.pop())
