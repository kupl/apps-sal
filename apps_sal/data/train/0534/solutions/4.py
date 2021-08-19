import sys
for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        (src, dest) = list(map(int, input().split()))
        adj[src].append(dest)
        adj[dest].append(src)
    print(max(max([len(a) for a in adj]), 3 if any((not set(adj[x]).isdisjoint(adj[y]) for x in range(len(adj)) for y in adj[x])) else max([len(a) for a in adj])))
