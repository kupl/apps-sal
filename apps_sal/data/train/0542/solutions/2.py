for _ in range(int(input())):
    (N, M) = map(int, input().split())
    array = []
    for i in range(N):
        array.append(list(input().strip()))
    count = 0
    for i in range(N - 1):
        for j in range(M - 1):
            for k in range(j + 1, min(j + N - i, M)):
                if array[i][j] == array[i][k] and array[i][j] == array[i + k - j][j] and (array[i][j] == array[i + k - j][k]):
                    count += 1
    print(count)
