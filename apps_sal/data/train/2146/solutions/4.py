(n, d, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
p = []
q = []
for x in a:
    if x > m:
        p.append(x)
    else:
        q.append(x)
p = [0] + sorted(p, reverse=True)
q = [0] + sorted(q, reverse=True)
for i in range(len(p) - 1):
    p[i + 1] += p[i]
for i in range(len(q) - 1):
    q[i + 1] += q[i]
ans = 0
for t in range(len(p)):
    v = n + d - t * d - t
    if 0 <= v < len(q) + d:
        ans = max(ans, p[t] + q[min(v, len(q) - 1)])
print(ans)
