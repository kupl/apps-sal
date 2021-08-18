def dfs(x, y):
    vis.append((x, y))
    y += 1
    nonlocal flag
    if flag or str.isalpha(grid[x][y]):
        return
    if y >= n - 1:
        flag = True
        return

    # stay idle
    if not str.isalpha(grid[x][y + 1]) and not str.isalpha(grid[x][y + 2]) and (x, y + 2) not in vis:
        dfs(x, y + 2)

    # move down
    if x > 0 and not str.isalpha(grid[x - 1][y]) and not str.isalpha(grid[x - 1][y + 1]) and not str.isalpha(grid[x - 1][y + 2]) and (x - 1, y + 2) not in vis:
        dfs(x - 1, y + 2)

    # move up
    if x < 2 and not str.isalpha(grid[x + 1][y]) and not str.isalpha(grid[x + 1][y + 1]) and not str.isalpha(grid[x + 1][y + 2]) and (x + 1, y + 2) not in vis:
        dfs(x + 1, y + 2)


T = int(input())
for loop in range(T):
    n, k = [int(i) for i in input().split()]
    grid = list()
    grid.append(input() + "    ")
    grid.append(input() + "    ")
    grid.append(input() + "    ")
    vis = list()
    flag = False
    for i in range(3):
        if grid[i][0] == 's':
            grid[i] = " " + grid[i][1:]
            dfs(i, 0)
            break
    if flag:
        print("YES")
    else:
        print("NO")
