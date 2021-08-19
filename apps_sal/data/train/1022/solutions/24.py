t = int(input())
for i in range(0, t):
    n = int(input())
    a = [int(i) for i in input().split()]
    if n % 2 != 0:
        print('NO')
    else:
        i = 0
        j = n // 2
        flag = 0
        while i < n // 2:
            if a[i] == -1 and a[j] != -1:
                a[i] = a[j]
            elif a[j] == -1 and a[i] != -1:
                a[j] = a[i]
            elif a[i] == -1 and a[j] == -1:
                a[i] = 1
                a[j] = 1
            elif a[i] != a[j]:
                flag = 1
                break
            i += 1
            j += 1
        if flag == 1:
            print('NO')
        else:
            print('YES')
            print(*a, sep=' ')
