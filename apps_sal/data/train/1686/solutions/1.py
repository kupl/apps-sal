MODULO = 20011

def solve(grid, R, C, d):
    if grid[1][1] == 0 or grid[R][C] == 0:
        return 0
    # count paths from (r=1, c=1) to (r=R, c=C)
    path_top = [[0] * (C + 1) for row in range(R + 1)]
    path_left = [[0] * (C + 1) for row in range(R + 1)]
    # 1st row:
    # from (1,1) going right, you can travel all the
    # way to (1,d+1) but no further than (1,C)
    for col in range(1, min(d + 2, C + 1)):
        if grid[1][col] == 1:
            path_left[1][col] = 1
        else:
            break
    # row-th row, row>1
    for row in range(2, R + 1):
        for col in range(1, C + 1):
            if grid[row][col] == 1:
                # entering (row,col) from the top:
                for i in range(1, min(d + 1, row)):
                    if grid[row - i][col] == 1:
                        path_top[row][col] += path_left[row - i][col]
                    else:
                        break
                # entering (row,col) from the left:
                for i in range(1, min(d + 1, col)):
                    if grid[row][col - i] == 1:
                        path_left[row][col] += path_top[row][col - i]
                    else:
                        break
    # return solution
    return path_top[R][C] + path_left[R][C]

def __starting_point():
    R, C, d = list(map(int, input().strip().split()))
    grid = [[0] * (C + 1) for row in range(R + 1)]
    for row in range(1, R + 1):
        grid[row] = [0] + list(map(int, input().strip().split()))
    print(solve(grid, R, C, d) % MODULO)

__starting_point()
