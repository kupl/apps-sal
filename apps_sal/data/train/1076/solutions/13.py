
# cook your dish here
def dist(a, b):
    if (a, b) in di:
        return di[(a, b)]
    if distance[a] < distance[b]:
        a, b = b, a
    c = distance[a] - distance[b]
    t = a
    while c:
        t = p[t]
        c -= 1
    w = b
    while t != w:
        t = p[t]
        w = p[w]
    di[(a, b)] = distance[a] + distance[b] - 2 * distance[t]
    return di[(a, b)]


t = int(input())
for t_iter in range(t):
    n, q = map(int, input().split())
    g = {}
    for i in range(n):
        g[i] = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    p = [None] * n
    distance = [-1] * n
    distance[0] = 0
    qu = [0]
    while len(qu):
        u = qu.pop(0)
        for v in g[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                p[v] = u
                qu.append(v)
    # print(p)
    # print(distance)
    di = {}
    for q_iter in range(q):
        a, da, b, db = map(int, input().split())
        a -= 1
        b -= 1
        flag = 0
        for i in range(n):
            if dist(a, i) == da and dist(b, i) == db:
                print(i + 1)
                flag = 1
                break
        if flag == 0:
            print(-1)
