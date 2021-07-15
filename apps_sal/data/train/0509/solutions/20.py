n, m = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = list(map(int, input().split()))
    g[u - 1].append((v - 1, c))
    g[v - 1].append((u - 1, c))
s = [0]
d = [1] * n
d[0] = 0
g2 = [[] for _ in range(n)]
while s:
    p = s.pop()
    for node, label in g[p]:
        if d[node]:
            d[node] = 0
            s.append(node)
            g2[p].append((node, label))
            g2[node].append((p, label))
s = [0]
d = [-1] * n
d[0] = 1
while s:
    p = s.pop()
    for node, label in g2[p]:
        if d[node] == -1:
            if d[p] == label:
                if label == n:
                    d[node] = 1
                else:
                    d[node] = label + 1
            else:
                d[node] = label
            s.append(node)
for x in d:
    print(x)

