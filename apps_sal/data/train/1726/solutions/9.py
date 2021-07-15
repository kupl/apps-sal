def path_finder(maze):
    grid = [list(v) for v in maze.split('\n')]
    n = len(grid)
    end = (n-1, n-1)
    def search(x, y):
        if (x,y) == end:
            return True
        elif grid[x][y] == 'W':
            return False
        elif grid[x][y] == 'V':
            return False

        grid[x][y] = 'V'

        if ((x < n-1 and search(x+1, y))
            or (y > 0 and search(x, y-1))
            or (x > 0 and search(x-1, y))
            or (y < n-1 and search(x, y+1))):

            return True

        return False

    return search(0,0)
