P = 910519
MOD = 32416190071
p = [1]
for i in range(1, 200010):
    p.append(P * p[i - 1] % MOD)
n = int(input())
s = list(set([input() for i in range(n)]))
n = len(s)
name = ['' for i in range(n)]
path = ['' for i in range(n)]
mp = {}
for i in range(n):
    link = s[i]
    j = link[7:].find('/')
    if j != -1:
        path[i] = link[j + 7:]
        name[i] = link[:j + 7]
    else:
        name[i] = link
for i in range(n):
    if path[i] not in mp:
        mp[path[i]] = len(mp)
h = {name[i]: 0 for i in range(n)}
for i in range(n):
    h[name[i]] += p[mp[path[i]]]
gp = {}
for (key, val) in list(h.items()):
    if val in gp:
        gp[val].append(key)
    else:
        gp[val] = [key]
ans = []
for (key, val) in list(gp.items()):
    if len(val) > 1:
        ans.append(val)
print(len(ans))
for a in ans:
    print(' '.join(a))
