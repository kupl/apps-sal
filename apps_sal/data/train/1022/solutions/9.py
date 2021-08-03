t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    dis = [int(x) for x in input().split()]
    if n % 2 == 1:
        print('NO')
        continue
    mid = n // 2
    for i in range(mid):
        if dis[i] == -1 and dis[mid + i] == -1:
            dis[i] = dis[i + mid] = 1
        elif dis[i] == -1:
            dis[i] = dis[i + mid]
        elif dis[i + mid] == -1:
            dis[i + mid] = dis[i]
    flag = True
    for i in range(mid):
        if dis[i] != dis[i + mid]:
            flag = False
            print('NO')
            break
    if flag:
        print('YES')
        for i in range(n):
            print(dis[i], end=' ')
        print()
