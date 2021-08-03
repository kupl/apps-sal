for _ in range(int(input())):
    res = 0
    mat = []
    n = int(input())
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(sorted(a))
    count = mat[n - 1][n - 1]
    temp = mat[n - 1][n - 1]
    c = 0
    k = 0
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            if mat[i][j] < temp:
                count += mat[i][j]
                temp = mat[i][j]
                c += 1
                break
        if c == 0:
            print(-1)
            k = 1
            break
        else:
            c = 0

    if k == 0:
        print(count)
