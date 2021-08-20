MAXX = 10 ** 9 + 1
N = eval(input())
nodes = list(map(int, input().split(' ')))
edges = [set() for _ in range(N)]
for _ in range(N - 1):
    (a, b) = list(map(int, input().split(' ')))
    edges[a - 1].add(b - 1)
    edges[b - 1].add(a - 1)
path = [[] for _ in range(N)]
(visited, tovisit) = (set(), [(0, 0)])
while tovisit:
    (p, v) = tovisit.pop()
    if v not in visited:
        path[v] = path[p] + [v]
        visited.add(v)
        news = edges[v] - visited
        tovisit.extend([(v, x) for x in news])
Q = eval(input())
for _ in range(Q):
    (q, a, b) = input().split(' ')
    (a, b) = (int(a) - 1, int(b) - 1)
    i = 1
    while i < min(len(path[a]), len(path[b])):
        if path[a][i] != path[b][i]:
            break
        i += 1
    s = path[a][i - 1:] + path[b][i:]
    if q == 'C':
        s = sorted([nodes[i] for i in s])
        d = s[-1] - s[0]
        for i in range(len(s) - 1):
            d = min(d, s[i + 1] - s[i])
        print(d)
    else:
        M = 0
        m = MAXX
        for i in range(len(s)):
            M = max(M, nodes[s[i]])
            m = min(m, nodes[s[i]])
        print(M - m)
