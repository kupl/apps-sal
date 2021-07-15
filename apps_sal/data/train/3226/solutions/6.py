def land_perimeter(grid):
    s, m = len(grid), len(grid[0])
    ans = 0
    for x in range(s):
        for y in range(m):
            if grid[x][y] == 'X':
                ans += 4
                if x < s - 1 and grid[x+1][y] == 'X':
                    ans -= 2
                if y < m - 1 and grid[x][y+1] == 'X':
                    ans -= 2
                    
    return ('Total land perimeter: {}'.format(ans))
