x = [int(w) for w in input().split()]
n = x[0]
x = x[1:]
a,p = x[:n],x[n:]

mgr = {i:1 for i in p}
if -1 in mgr:
    mgr[-1] = 0

d = []
for i in range(n):
    t = [0]
    par = p[i]
    while mgr.get(par,0):
        t.append(a[par-1])
        par = p[par-1]
    d.append(max(t)-a[i])

print(max(d))
