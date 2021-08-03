# cook your dish here

t = int(input())
i = 0
for i in range(t):
    n = int(input())
    a = list(map(str, input().split()))
    a.sort()
    z = set(a)
    # print(z)
    q = list(z)
    q.sort()
    # print(q)
    b = []
    k = 0
    # print(max(a))
    for j in q:
        var = a.count(j)
        b.append(var)
        # b[k].append(a.count(j))

        # k+=1

    print(q[b.index(max(b))])
