import sys

sys.setrecursionlimit(6500)


def find(n):
    if d[n] < 0:
        return n
    else:
        d[n] = find(d[n])
        return d[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    if d[a] <= d[b]:
        d[a] += d[b]
        d[b] = a
    else:
        d[b] += d[a]
        d[a] = b
    return True


def members(n):
    p = find(n)
    ans = []
    for i in range(N):
        if find(i) == p:
            ans.append(i)
    return ans


def same(a, b):
    if find(a) == find(b):
        return True
    else:
        return False


N, M = map(int, input().split())
p = list(map(int, input().split()))

d = [-1] * N

for i in range(M):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    union(x, y)

q = [-1] * N
for i in range(N):
    q[p[i] - 1] = i
ans = 0
for i in range(N):
    if same(i, q[i]):
        ans += 1
print(ans)
