(n, k) = map(int, input().split())
x = []
for _ in range(n):
    x.append(set([int(w) for w in input().split()][1:]))
vis = {}
vis[0] = True
q = [x[0]]
for ele in q:
    for j in range(n):
        if not vis.get(j, False):
            if len(ele.intersection(x[j])) >= k:
                q.append(x[j])
                vis[j] = True
print(len(q))
