def solve(grid, row, col, white):
    s = 0
    for thing in grid[row]:
        for i in range(col, len(grid[row])):
            if grid[row][i] == 'B':
                s = i - col + 1
                return s
            elif grid[row][i] == 'W':
                white += 1
            if white == 2:
                s = i - col + 1
                return s
            if i + 1 == len(grid[row]):
                s = i - col + 1
                return s
    return s


array = [int(x) for x in input().split()]
(n, m, w, b) = (array[0], array[1], array[2], array[3])
array = array[4:]
white = []
black = []
grid = [['.' for i in range(m)] for j in range(n)]
for i in range(0, 2 * w - 1, 2):
    grid[array[i] - 1][array[i + 1] - 1] = 'W'
for i in range(2 * w, len(array) - 1, 2):
    grid[array[i] - 1][array[i + 1] - 1] = 'B'
s = 0
for i in range(n):
    current = 0
    for j in range(m):
        if grid[i][j] == 'W' or grid[i][j] == 'B':
            current = 0
            continue
        if current == 0:
            current = solve(grid, i, j, 0)
            s += current
        else:
            current -= 1
            s += current
print(s)
