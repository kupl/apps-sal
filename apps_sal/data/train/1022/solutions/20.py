tc = int(input())
for x in range(tc):
    n = int(input())
    a = [int(x) for x in input().split()]
    if n % 2 != 0:
        print('NO')
    else:
        a1 = a[:n // 2]
        a2 = a[n // 2:]
        t = 0
        for i in range(n // 2):
            if a1[i] != -1 and a2[i] != -1 and (a1[i] != a2[i]):
                print('NO')
                t = 1
                break
            else:
                if a1[i] == -1 and a2[i] != -1:
                    a1[i] = a2[i]
                if a2[i] == -1 and a1[i] != -1:
                    a2[i] = a1[i]
                if a1[i] == -1 and a2[i] == -1:
                    a1[i] = a2[i] = 1
        if t == 0:
            print('YES')
            print(*a1 + a2)
