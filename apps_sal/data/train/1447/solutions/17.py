t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    d = {}
    flag = 0
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = [i, 1]
        elif a[i] in d and d[a[i]][0] + 1 == i:
            temp = d[a[i]][1]
            d[a[i]] = [i, temp + 1]
        else:
            print('NO')
            flag = 1
            break
    vals = list(d.values())
    dist = []
    for i in vals:
        dist.append(i[1])
    if flag == 0:
        if len(dist) == len(set(dist)):
            print('YES')
        else:
            print('NO')
