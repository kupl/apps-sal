for _ in range(int(input())):
    n = int(input())
    l = []
    x = set()
    res = 0
    for z in range(n):
        xi, yi = (list(map(int, input().split())))
        x.add(xi)
        l.append([xi, yi])
    l.sort(reverse=True, key=lambda q: q[1])
    if len(x) < 3:
        res = 0
    else:
        temp = []
        for i in range(n):
            if len(temp) == 3:
                break
            elif l[i][0] in temp:
                continue
            else:
                res += l[i][1]
                temp.append(l[i][0])
    print(res)
