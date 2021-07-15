n = int(input())
d = dict()
for i in range(n):
    s = input().strip()
    s = s[7:]
    f = s.find('/')
    if f != -1:
        a = s[:f]
        b = s[f:]
    else:
        a = s
        b = ''
    if a in d:
        d[a].add(b)
    else:
        d[a] = {b}
ans = dict()
for i in d:
    x = sorted(d[i])
    x = list(x)
    x = '*'.join(x)
    d[i] = x
    if x in ans:
        ans[x].append(i)
    else:
        ans[x] = [i]
ans2 = []
ansc = 0
for i in ans:
    if len(ans[i]) > 1:
        ansc += 1
        ans2.append(' '.join(map(lambda x: 'http://'+x, ans[i])))
print(ansc)
for i in ans2:
    print(i)
