x = [int(w) for w in input().split()]
n = x[0]
x = x[1:]
(a, p) = (x[:n], x[n:])
x = [[] for i in range(n)]
q = []
for i in range(n):
    if p[i] == -1:
        q.append([i, a[i]])
    else:
        x[p[i] - 1].append(i)
ans = float('-inf')
while q:
    (i, mx) = q[-1]
    q.pop()
    ans = max(ans, mx - a[i])
    mx = max(mx, a[i])
    for j in x[i]:
        q.append([j, mx])
print(ans)
