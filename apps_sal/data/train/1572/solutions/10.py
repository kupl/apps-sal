x = [int(w) for w in input().split()]
n = x[0]
x = x[1:]
a = {i + 1: x[i] for i in range(n)}
p = {i + 1: x[n + i] for i in range(n)}
mgr = {i: 1 for i in p}
if -1 in mgr:
    mgr[-1] = 0
d = []
for i in range(1, n + 1):
    t = [float('-inf')]
    par = p[i]
    while mgr.get(par, 0):
        t.append(a[par])
        par = p[par]
    p[i] = -1
    d.append(max(t) - a[i])
    a[i] = max(t)
print(max(d))
