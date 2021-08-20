t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        temp = []
        temp = list(map(int, input().strip().split()))
        temp.sort()
        grid.append(temp)
    curr = max(grid[n - 1])
    total = curr
    for i in range(n - 2, 0 - 1, -1):
        flag = 0
        for j in range(n - 1, 0 - 1, -1):
            if grid[i][j] < curr:
                flag = 1
                curr = grid[i][j]
                total += curr
                break
        if flag == 0:
            total = -1
            break
    print(total)
