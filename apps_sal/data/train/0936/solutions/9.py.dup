t = int(input())
while t > 0:
    n = int(input())
    mat = []
    for i in range(n):
        l = [int(x) for x in input().split()]
        mat.append(l)
    # print(mat)
    c = 0
    for i in range(n - 1, -1, -1):
        if(mat[0][i] != i + 1):
            c += 1
            for j in range(i + 1):
                mat[0][j], mat[j][0] = mat[j][0], mat[0][j]
    print(c)
    t -= 1
