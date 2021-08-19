for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    flag = 0
    if n % 2 == 1:
        print('NO')
        continue
    for i in range(n // 2):
        x = l[i]
        y = l[i + n // 2]
        if x == -1 or y == -1:
            l[i] = max(x, y, 1)
            l[i + n // 2] = l[i]
        elif x != y:
            flag = 1
    if flag == 1:
        print('NO')
    else:
        print('YES')
        for i in l:
            print(i, end=' ')
        print('')
