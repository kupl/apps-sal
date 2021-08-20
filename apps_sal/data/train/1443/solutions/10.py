for _ in range(int(input())):
    (N, M) = list(map(int, input().split(' ')))
    grid = []
    for x in range(N):
        row = [i for i in input()]
        grid.append(row)
    collisions = 0
    for x in range(M):
        z = 0
        for y in range(N):
            if grid[y][x] == '1':
                z += 1
        if z == 2:
            collisions += 1
        elif z > 2:
            collisions += z * (z - 1) // 2
    print(collisions)
