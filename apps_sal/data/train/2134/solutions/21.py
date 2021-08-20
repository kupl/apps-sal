from collections import defaultdict, deque
n = int(input())
p = [0, 0] + list(map(int, input().split()))
s = [0] + list(map(int, input().split()))
ht = [0] * (n + 1)
ht[1] = 1
gr = defaultdict(list)
for i in range(2, n + 1):
    gr[p[i]].append(i)
q = deque()
q.append([1, -1])
while q:
    (x, pr) = q.popleft()
    for i in gr[x]:
        if i != pr:
            ht[i] = ht[x] + 1
            q.append([i, x])
a = [0] * (n + 1)
a[1] = s[1]
q.append([1, -1])
while q:
    (x, pr) = q.popleft()
    for ch in gr[x]:
        q.append([ch, x])
    if ht[x] % 2 == 0:
        mn = float('inf')
        for i in gr[x]:
            mn = min(mn, s[i] - s[p[x]])
        if mn != float('inf'):
            a[x] = mn
        for i in gr[x]:
            a[i] = s[i] - s[p[x]] - mn
tf = True
for i in a:
    if i < 0:
        tf = False
        break
if tf:
    print(sum(a))
else:
    print(-1)
