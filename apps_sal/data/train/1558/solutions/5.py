def destroy_cells(N, M):
    print(N * M, end=' ')
    for k in range(1, N * M - 1):
        (row, col, i, j) = (0, 0, 0, 0)
        positions = [(0, 0)]
        while row < N or col < M:
            j = j + k + 1
            if j >= M:
                row += j // M
            if row < N:
                j = j % M
                positions.append((row, j))
            i = i + k + 1
            if i >= N:
                col += i // N
            if col < M:
                i = i % N
                positions.append((i, col))
        positions = set(positions)
        print(len(positions), end=' ')
    print(1)


test = int(input())
for i in range(test):
    (N, M) = map(int, input().split())
    destroy_cells(N, M)
