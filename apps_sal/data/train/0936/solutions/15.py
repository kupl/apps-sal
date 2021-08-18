t = int(input())
for i in range(t):
    n = int(input())
    mat = []
    for j in range(0, n):
        a = list(map(int, input().split()))
        mat.append(a)
    count, flag = 0, 0
    for j in range(1, n + 1):
        if flag == 0:
            if mat[0][n - j] != (n - j + 1):
                count += 1
                flag += 1
        if flag == 1:
            if mat[n - j][0] != (n - j + 1):
                count += 1
                flag = 0
    print(count)
