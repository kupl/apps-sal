n = int(input())
e = []
v = []
for i in range(n - 1):
    e.append(list(map(int, input().split())))
c = [-1] + list(map(int, input().split()))
for i in e:
    if c[i[0]] != c[i[1]]:
        v.append(i)
if not v:
    print('YES')
    print(1)
else:
    s = set(v[0])
    list([s.intersection_update(set(x)) for x in v])
    if s:
        print('YES')
        print(list(s)[0])
    else:
        print('NO')
