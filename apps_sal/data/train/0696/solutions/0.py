t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    k = []
    for i in range(m):
        a, b = list(map(int, input().split()))
        k.append([a, b])
    k.sort()
    c = []
    flag = 1
    x = k[0][0]
    y = k[0][1]

    for i in k[1:]:
        if i[0] <= y:
            y = max(y, i[1])
        else:
            c.append([x - 1, y - 1])
            x = i[0]
            y = i[1]
    c.append([x - 1, y - 1])
    m = []
    j = 0

    for i in c:
        while j < i[0]:
            m.append(l[j])
            j += 1
        x = l[i[0]:i[1] + 1]
        m += sorted(x)
        j = i[1] + 1

    while j < n:
        m.append(l[j])
        j += 1

    if m == sorted(l):
        print('Possible')
    else:
        print('Impossible')
