t = int(input())
for i in range(t):
    n = int(input())
    matrix = []
    for j in range(n):
        s = input()
        matrix.append(s)
    failflag = 0
    for x in range(n):
        for y in range(n):
            if matrix[x][y] == '1' and x < n - 1 and y < n - 1:
                if matrix[x + 1][y] == '0' and matrix[x][y + 1] == '0':
                    failflag = 1
    if failflag == 0:
        print('YES')
    else:
        print('NO')
