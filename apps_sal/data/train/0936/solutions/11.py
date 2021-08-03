for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    count = 0
    for i in reversed(list(range(n))):
        if count & 1:
            if matrix[0][i] != i * n + 1:
                count += 1
        else:
            if matrix[i][0] != i * n + 1:
                count += 1
    print(count)
