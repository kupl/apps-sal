for t in range(int(input())):
    l = sorted(list(map(int, input().split())))
    if l[0] ** 2 + l[1] ** 2 == l[2] ** 2 and l[0] + l[1] >= l[2] and (l[0] > 0) and (l[1] > 0) and (l[2] > 0):
        print('YES')
    else:
        print('NO')
