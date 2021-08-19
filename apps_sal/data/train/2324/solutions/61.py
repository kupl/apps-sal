(N,) = list(map(int, input().split()))
G = [set() for _ in range(N + 1)]
for i in range(N - 1):
    (A, B) = list(map(int, input().split()))
    G[A].add(B)
    G[B].add(A)
path = []
stack = [1]
vs = set()
while stack:
    v = stack.pop()
    if v > 0:
        vs.add(v)
        path.append(v)
        for u in G[v]:
            if u in vs:
                continue
            if u == N:
                stack = []
                path.append(u)
                break
            stack += [-v, u]
    else:
        path.pop()
x = path[-(-len(path) // 2)]
stack = [1]
vs = set()
while stack:
    v = stack.pop()
    vs.add(v)
    for u in G[v]:
        if u in vs:
            continue
        if u == x:
            continue
        stack.append(u)
x = len(vs) - 1
y = N - 2 - x
if x > y:
    print('Fennec')
else:
    print('Snuke')
