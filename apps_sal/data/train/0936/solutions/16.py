t = int(input())
while t > 0:
    n = int(input())
    matrix = []
    for i in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
    bool = [False for i in range(n)]
    for i in range(n):
        if matrix[0][i] == i + 1:
            bool[i] = True
    count = 0
    k = n - 1
    while k >= 1:
        if bool[k] == False:
            count += 1
            for i in range(k + 1):
                for j in range(i, k + 1):
                    (matrix[i][j], matrix[j][i]) = (matrix[j][i], matrix[i][j])
            for i in range(n):
                if matrix[0][i] == i + 1:
                    bool[i] = True
                else:
                    bool[i] = False
        k -= 1
    print(count)
    t -= 1
