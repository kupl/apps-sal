t = int(input())
i = 0
for i in range(t):
    n = int(input())
    a = list(map(str, input().split()))
    a.sort()
    z = set(a)
    q = list(z)
    q.sort()
    b = []
    k = 0
    for j in q:
        var = a.count(j)
        b.append(var)
    print(q[b.index(max(b))])
