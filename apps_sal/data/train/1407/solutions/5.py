def update(grid, i, j, k):
    used = [0] * 6
    # 0 -2 -2 0 -1 1 -1 -1
    if j - 2 >= 0:
        used[grid[i][j - 2]] = 1
    if i - 2 >= 0:
        used[grid[i - 2][j]] = 1
    if i - 1 >= 0 and j - 1 >= 0:
        used[grid[i - 1][j - 1]] = 1
    if i - 1 >= 0 and j + 1 < len(grid[0]):
        used[grid[i - 1][j + 1]] = 1

##    print("%d %d" % (i, j))
# print(used)
# print(grid)
    # return the first available value
    #print("k: %d" % k)
    for fill in range(1, 5):
        if used[fill] == 0:
            if fill > k:
                k = fill
            grid[i][j] = fill
            return k
    # This shouldn't happen
    grid[i][j] = 5
    return 5


grid5050 = [[0] * 50 for row in range(50)]
k = 1
for i in range(50):
    for j in range(50):
        k = update(grid5050, i, j, k)
noOfCases = int(input())
for case in range(noOfCases):
    # Read in data for each case
    n, m = list(map(int, input().split()))
    #print("N and M %d %d" % (n,m))
    k = 1
    grid = [[0] * m for row in range(n)]

    if n >= 3 and m >= 3:
        k = 4
        for i in range(n):
            for j in range(m):
                grid[i][j] = grid5050[i][j]
    elif n == 2 and m > 2:
        # this case i missed??
        k = 3
        for j in range(m):
            next = j % 3 + 1
            grid[0][j] = next
            grid[1][j] = next
    else:
        for i in range(n):
            for j in range(m):
                k = update(grid, i, j, k)

    print(k)
    print(('\n'.join([''.join([(str(item) + ' ') for item in row])
                      for row in grid])))
