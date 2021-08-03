q = int(input())
for i in range(q):
    n = int(input())
    tube = [[0] * 2 for i in range(n + 1)]
    a = [int(x) for x in list(input())]
    b = [int(x) for x in list(input())]
    k = 0
    for i in range(n):
        if a[i] == 1 or a[i] == 2:
            tube[i][0] = 1
        if b[i] == 1 or b[i] == 2:
            tube[i][1] = 1
    for i in range(n):
        if tube[i][k] == 0:
            if tube[i][(k + 1) % 2] == 0:
                k = (k + 1) % 2
            else:
                print('NO')
                break
    else:
        if k == 0:
            print('NO')
        else:
            print('YES')
