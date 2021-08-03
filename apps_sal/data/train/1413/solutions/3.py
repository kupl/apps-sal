from math import inf

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    r, c = map(int, input().split())
    grid = [[False] * (m + 2) for __ in range(n + 2)]
    for i in range(n):
        s = input()
        for j, x in enumerate(s):
            grid[i][j] = x == '1'
    solution = [[[inf, inf, inf] for ___ in range(m)] for __ in range(n)]
    r -= 1
    c -= 1
    solution[r][c][0] = 0
    touched_set = set()
    touched_set.add((r, c, 0))
    while len(touched_set):
        new_touched_set = set()
        while len(touched_set):
            r, c, o = touched_set.pop()
            new_sol = 1 + solution[r][c][o]
            if o == 0:
                if grid[r][c + 1] and grid[r][c + 2] and solution[r][c + 1][1] > new_sol:
                    solution[r][c + 1][1] = new_sol
                    new_touched_set.add((r, c + 1, 1))
                if grid[r + 1][c] and grid[r + 2][c] and solution[r + 1][c][2] > new_sol:
                    solution[r + 1][c][2] = new_sol
                    new_touched_set.add((r + 1, c, 2))
                if grid[r][c - 2] and grid[r][c - 1] and solution[r][c - 2][1] > new_sol:
                    solution[r][c - 2][1] = new_sol
                    new_touched_set.add((r, c - 2, 1))
                if grid[r - 2][c] and grid[r - 1][c] and solution[r - 2][c][2] > new_sol:
                    solution[r - 2][c][2] = new_sol
                    new_touched_set.add((r - 2, c, 2))
            elif o == 1:
                if grid[r][c + 2] and solution[r][c + 2][0] > new_sol:
                    solution[r][c + 2][0] = new_sol
                    new_touched_set.add((r, c + 2, 0))
                if grid[r + 1][c] and grid[r + 1][c + 1] and solution[r + 1][c][1] > new_sol:
                    solution[r + 1][c][1] = new_sol
                    new_touched_set.add((r + 1, c, 1))
                if grid[r][c - 1] and solution[r][c - 1][0] > new_sol:
                    solution[r][c - 1][0] = new_sol
                    new_touched_set.add((r, c - 1, 0))
                if grid[r - 1][c] and grid[r - 1][c + 1] and solution[r - 1][c][1] > new_sol:
                    solution[r - 1][c][1] = new_sol
                    new_touched_set.add((r - 1, c, 1))
            else:
                if grid[r][c + 1] and grid[r + 1][c + 1] and solution[r][c + 1][2] > new_sol:
                    solution[r][c + 1][2] = new_sol
                    new_touched_set.add((r, c + 1, 2))
                if grid[r + 2][c] and solution[r + 2][c][0] > new_sol:
                    solution[r + 2][c][0] = new_sol
                    new_touched_set.add((r + 2, c, 0))
                if grid[r][c - 1] and grid[r + 1][c - 1] and solution[r][c - 1][2] > new_sol:
                    solution[r][c - 1][2] = new_sol
                    new_touched_set.add((r, c - 1, 2))
                if grid[r - 1][c] and solution[r - 1][c][0] > new_sol:
                    solution[r - 1][c][0] = new_sol
                    new_touched_set.add((r - 1, c, 0))
        touched_set = new_touched_set

    for i in range(n):
        for j in range(m):
            print(solution[i][j][0] if solution[i][j][0] != inf else -1, end=' ')
        print()
