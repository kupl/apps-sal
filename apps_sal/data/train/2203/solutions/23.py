n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    is_dif = True
    for j in range(n):
        c = a[i].count(a[i][j])
        if c > 1:
            is_dif = False
            break
    if is_dif:
        for k in range(n):
            if a[i][k] == 0:
                a[i][k] = n
            print(a[i][k], end=' ')
        break
