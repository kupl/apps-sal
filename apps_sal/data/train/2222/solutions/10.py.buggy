t = int(input())
for test in range(t):
    n, k = [int(i) for i in input().split()]
    grid = [[True for i in range(3)] for i in range(n)]
    ok = [[False for i in range(3)] for i in range(n)]
    #x-col, y-row

    rx = 0
    ry = 0
    for i in range(3):
        row = input()
        j = 0
        for v in row:
            if v == 's':
                # print("here")
                rx = j
                ry = i
            elif v != '.':
                grid[j][i] = False
            j += 1

    def verify(x, y):
        if x < n and y < 3 and x >= 0 and y >= 0:
            return grid[x][y]
        else:
            return False

    def dfs(x, y):
        nonlocal ok
        if not ok[x][y]:
            #print(x,' ',y)
            ok[x][y] = True
            if verify(x + 1, y) and verify(x + 3, y):
                dfs(x + 3, y)
            if verify(x + 1, y) and verify(x + 1, y + 1) and verify(x + 3, y + 1):
                dfs(x + 3, y + 1)
            if verify(x + 1, y) and verify(x + 1, y - 1) and verify(x + 3, y - 1):
                dfs(x + 3, y - 1)

            # end game(tap in)
            if x + 2 >= n - 1:
                if verify(x + 1, y):
                    dfs(x + 1, y)

    dfs(rx, ry)
    #print(rx, ry)
    # print(ok)

    res = False
    for i in range(3):
        if ok[n - 1][i]:
            res = True

    if res:
        print("YES")
    else:
        print("NO")
