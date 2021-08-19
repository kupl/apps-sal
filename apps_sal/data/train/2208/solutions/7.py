def find(x):
    x1 = x
    while p[x] != x:
        x = p[x]
    while p[x1] != x1:
        x2 = p[x1]
        p[x1] = x
        x1 = x2
    return x


def inp():
    return list(map(int, input().split()))


(n, k) = inp()
edges = []
for i in range(k):
    (x, y) = inp()
    edges.append([x - 1, y - 1])
p = [i for i in range(n)]
ans = 0
for i in edges:
    p1 = find(i[0])
    p2 = find(i[1])
    if p1 == p2:
        ans += 1
    else:
        p[p1] = p2
print(ans)
