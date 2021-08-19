def path_finder(maze):
    maze = [list('W' + string + 'W') for string in maze.split('\n')]
    n = len(maze[0])
    maze = [['W'] * n] + maze + [['W'] * n]
    visited = {(i, j): 0 for i in range(n) for j in range(n)}
    visited[1, 1] = 1
    stack = [(1, 1)]
    while len(stack) > 0:
        (idx1, idx2) = stack.pop()
        if idx1 == n - 2 and idx2 == n - 2:
            return True
        if maze[idx1 - 1][idx2] == '.' and visited[idx1 - 1, idx2] == 0:
            visited[idx1 - 1, idx2] = 1
            stack.append((idx1 - 1, idx2))
        if maze[idx1][idx2 - 1] == '.' and visited[idx1, idx2 - 1] == 0:
            visited[idx1, idx2 - 1] = 1
            stack.append((idx1, idx2 - 1))
        if maze[idx1][idx2 + 1] == '.' and visited[idx1, idx2 + 1] == 0:
            visited[idx1, idx2 + 1] = 1
            stack.append((idx1, idx2 + 1))
        if maze[idx1 + 1][idx2] == '.' and visited[idx1 + 1, idx2] == 0:
            visited[idx1 + 1, idx2] = 1
            stack.append((idx1 + 1, idx2))
    return False
