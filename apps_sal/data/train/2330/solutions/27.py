def no():
    print(-1)
    return


s = input()
n = len(s)
if s[-1] == '1':
    no()
s = s[:-1]
if s != s[::-1]:
    no()
if s[0] == '0':
    no()
li = [0]
adj = [[] for _ in range(n + 1)]
for (v, e) in enumerate(s, 1):
    if e == '1':
        for u in li:
            adj[u].append(v)
        li = []
    li.append(v)
adj[n - 1].append(n)
for (u, vs) in enumerate(adj[1:], 1):
    for v in vs:
        print((u, v))
