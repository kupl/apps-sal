nr = int(input())
d = {}
for r in range(nr):
    (s, v) = list(map(str, input().split()))
    d[int(v)] = s
q = int(input())
lis = []
for i in range(q):
    lis.append(input())
l = list(d.keys())
l.sort(reverse=True)
ans = 'NO'
for j in lis:
    ans = 'NO'
    for k in l:
        if len(j) <= len(d[k]):
            a = d[k]
            if j == a[0:len(j)]:
                ans = a
                break
    print(ans)
