for __ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 0 or a[1] == 0 or a[2] == 0:
        print('NO')
    elif a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
        print('YES')
    else:
        print('NO')
