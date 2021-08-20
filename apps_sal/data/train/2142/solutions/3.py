n = int(input())
if n == 1:
    print(0)
else:
    m = [[0] * n] * n
    a = [int(0)] * n
    for i in range(0, n):
        m[i] = input().split()
        a[i] = int(m[i][(i + 1) % n])
        for j in range(0, n):
            if j != i:
                a[i] = a[i] | int(m[i][j])
    for i in range(0, n):
        print(a[i], end=' ')
