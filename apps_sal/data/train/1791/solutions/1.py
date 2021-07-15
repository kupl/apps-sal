# Return the array of movements to execute to get out of the maze

def first_position(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] in "><^v":
                return (i, j)

def walking(maze, passed, path, x, y, move):
    lin, col = len(maze), len(maze[0])
    if x < 0 or x >= lin or y < 0 or y >= col:
        return True
    if maze[x][y] == '#' or passed[x][y]:
        return False
    passed[x][y] = True
    
    if move == '>':
        r = walking(maze, passed, path, x+1, y, 'v')
        l = walking(maze, passed, path, x-1, y, '^')
        f = walking(maze, passed, path, x, y+1, '>')
        b = walking(maze, passed, path, x, y-1, '<')
    elif move == '<':
        r = walking(maze, passed, path, x-1, y, '^')
        l = walking(maze, passed, path, x+1, y, 'v')
        f = walking(maze, passed, path, x, y-1, '<')
        b = walking(maze, passed, path, x, y+1, '>')
    elif move == '^':
        r = walking(maze, passed, path, x, y+1, '>')
        l = walking(maze, passed, path, x, y-1, '<')
        b = walking(maze, passed, path, x+1, y, 'v')
        f = walking(maze, passed, path, x-1, y, '^')
    elif move == 'v':
        r = walking(maze, passed, path, x, y-1, '<')
        l = walking(maze, passed, path, x, y+1, '>')
        b = walking(maze, passed, path, x-1, y, '^')
        f = walking(maze, passed, path, x+1, y, 'v')
    
    if f:
        path += ["F"]
    elif b:
        path += ["F", "B"]
    elif r:
        path += ["F", "R"]
    elif l:
        path += ["F", "L"]
    
    return f or b or r or l

def escape(maze):
    path = []
    passed = [[False for j in range(len(maze[0]))] for i in range(len(maze))]
    i, j = first_position(maze)
    walking(maze, passed, path, i, j, maze[i][j])
    return path[::-1]
