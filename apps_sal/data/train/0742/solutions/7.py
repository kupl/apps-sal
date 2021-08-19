t = int(input())
for _ in range(t):
    coef = list(map(int, input().split()))
    mpow = len(coef) - 1
    row1 = []
    row2 = []
    mat = []
    for i in range(len(coef)):
        if i % 2 == 0:
            row1.append(coef[i])
        else:
            row2.append(coef[i])
    if len(coef) % 2:
        row2.append(0)
    mat.append(row1)
    mat.append(row2)
    idle = [0] * len(row1)
    for i in range(2, len(coef)):
        rown = []
        for j in range(1, len(row1)):
            val = mat[i - 1][0] * mat[i - 2][j] - mat[i - 2][0] * mat[i - 1][j]
            rown.append(val)
        for _ in range(len(rown), len(row1)):
            rown.append(0)
        mat.append(rown)
        if rown == idle:
            for i in range(len(mat)):
                if mat[i] == idle:
                    for j in range(len(mat[i])):
                        mat[i][j] = mat[i - 1][j] * (mpow + 4 - (i + 1) - 2 * (j + 1))
    s = 0
    sa = 0
    for i in mat:
        s += i[0]
        sa += abs(i[0])
    c = 0
    'for i in range(len(mat)):\n        if mat[i]==idle:\n            for j in range(len(mat[i])):\n                mat[i][j] = mat[i-1][j]*(mpow+4-(i+1)-2*(j+1))'
    if s == sa:
        c = 1
        for i in range(len(mat)):
            if mat[i][0] == 0:
                c = 0
                break
    print(c)
