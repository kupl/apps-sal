n = int(input())
L = [[] for i in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    L[a - 1].append(b - 1)
    L[b - 1].append(a - 1)
l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
W = []
for i in range(n):
    W.append(abs(l[i] - l1[i]))
was = [0 for i in range(n)]
q = [[0, 0, 0]]
ans = []
while q:
    e = q[0]
    was[e[0]] = 1
    if e[1] != W[e[0]]:
        ans.append(e[0] + 1)
        e[1] = 1 - e[1]
    for x in L[e[0]]:

        if was[x] == 0:
            q.append([x, e[2], e[1]])
    del q[0]
print(len(ans))
print('\n'.join(map(str, ans)))
