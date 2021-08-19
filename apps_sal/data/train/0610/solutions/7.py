t = int(input())
for i in range(t):
    n = int(input())
    a = []
    a = list(map(int, input().split()))
    x = []
    for j in range(n):
        if a[j] == 1:
            x.append(j)
    k = len(x)
    flag = 0
    for j in range(k - 1):
        if abs(x[j] - x[j + 1]) < 6:
            flag = 1
            break
    if flag == 0:
        print('YES')
    else:
        print('NO')
