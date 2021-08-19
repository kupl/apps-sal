def path_finder(maze):  # DFS
    # Create a matrix of given stringMaze and add walls around it

    maze = [list("W" + string + "W") for string in maze.split('\n')]
    n = len(maze[0])
    maze = [['W'] * n] + maze + [['W'] * n]

    #################################################

    # Create Visited dict with indexes as keys

    visited = {(i, j): 0 for i in range(n) for j in range(n)}
    visited[(1, 1)] = 1

    #################################################

    # Stack to store DFS info as index tuples
    stack = [(1, 1)]
    while len(stack) > 0:
        idx1, idx2 = stack.pop()

        if idx1 == n - 2 and idx2 == n - 2:  # (ง°ل͜°)ง
            return True

        if maze[idx1 - 1][idx2] == '.' and visited[(idx1 - 1, idx2)] == 0:
            visited[(idx1 - 1, idx2)] = 1
            stack.append((idx1 - 1, idx2))

        if maze[idx1][idx2 - 1] == '.' and visited[(idx1, idx2 - 1)] == 0:
            visited[(idx1, idx2 - 1)] = 1
            stack.append((idx1, idx2 - 1))

        if maze[idx1][idx2 + 1] == '.' and visited[(idx1, idx2 + 1)] == 0:
            visited[(idx1, idx2 + 1)] = 1
            stack.append((idx1, idx2 + 1))

        if maze[idx1 + 1][idx2] == '.' and visited[(idx1 + 1, idx2)] == 0:
            visited[(idx1 + 1, idx2)] = 1
            stack.append((idx1 + 1, idx2))

    return False
