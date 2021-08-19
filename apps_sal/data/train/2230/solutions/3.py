n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
t = [[p[i], a[i], b[i], 1] for i in range(n)]
t = sorted(t, key=lambda x: x[0])
p = [0, 0, 0, 0]
ans = []
for i in range(m):
    clr = c[i]
    while p[clr] < n and (t[p[clr]][3] == 0 or (t[p[clr]][1] != clr and t[p[clr]][2] != clr)):
        p[clr] += 1
    if p[clr] == n:
        ans.append(-1)
    else:
        t[p[clr]][3] = 0
        ans.append(t[p[clr]][0])
print(' '.join([str(a) for a in ans]))
