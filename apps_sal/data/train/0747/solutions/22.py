for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    flag = 0
    if a[n - 1] == a[n - 2]:
        print('NO')
        continue
    i = 0
    while i < n - 2:
        if a[i] == a[i + 2]:
            flag = 1
            break
        elif a[i] == a[i + 1]:
            b.append(a.pop(i))
            n = n - 1
        i += 1
    if flag == 0:
        b.sort(reverse=True)
        print('YES')
        print(*a + b)
    else:
        print('NO')
