t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if n % 2 != 0:
        print('NO')
        continue
    x = n // 2
    possible = True
    for i in range(x):
        if a[i] == -1:
            if a[i + x] == -1:
                a[i] = a[i + x] = 1
            else:
                a[i] = a[i + x]
        elif a[i + x] == -1:
            a[i + x] = a[i]
        elif a[i] != a[i + x]:
            possible = False
            break
    if possible:
        print('YES')
        for x in a:
            print(x, end=' ')
        print()
    else:
        print('NO')
