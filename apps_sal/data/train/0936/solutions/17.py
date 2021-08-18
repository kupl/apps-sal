t = int(input())
for test in range(t):
    n = int(input())
    matrix = []
    count = 0
    for i in range(n):
        A = list(map(int, input().split()))
        matrix.append(A)

    for i in range(n - 1, 0, -1):
        if matrix[0][i] != i + 1:
            count += 1
            for j in range(i, 0, -1):
                temp = matrix[0][j]
                matrix[0][j] = matrix[j][0]
                matrix[j][0] = temp

    print(count)
