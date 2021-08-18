def find_path(x, y):
    p1, p2 = [], []
    while x != 0:
        p1.append(x)
        x = x // 2
    while y != 0:
        p2.append(y)
        y = y // 2
    p1 = p1[::-1]
    p2 = p2[::-1]
    for i in range(min(len(p1), len(p2))):
        if p1[i] == p2[i]:
            ind = i
        else:
            break
    path = []
    for i in range(ind, len(p1)):
        path.append(p1[i])
    path = path[::-1]
    for i in range(ind + 1, len(p2)):
        path.append(p2[i])

    return path


q = int(input())
cost = {}
for i in range(q):
    a = list(map(int, input().split()))
    b = find_path(a[1], a[2])
    if a[0] == 1:
        w = a[-1]
        for j in range(1, len(b)):
            if (b[j], b[j - 1]) not in cost:
                cost[(b[j], b[j - 1])] = w
                cost[(b[j - 1], b[j])] = w
            else:
                cost[(b[j], b[j - 1])] += w
                cost[(b[j - 1], b[j])] += w
    else:
        ans = 0
        for j in range(1, len(b)):
            if (b[j], b[j - 1]) in cost:
                ans += cost[(b[j], b[j - 1])]
        print(ans)
