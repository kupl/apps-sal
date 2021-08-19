def path_finder(maze):
    maze = maze.split('\n')
    home = (len(maze) - 1, len(maze) - 1)
    M = {(r, c) for r in range(len(maze)) for c in range(len(maze)) if maze[r][c] == '.'} - {(0, 0)}
    P = {(0, 0)}
    while P and home not in P:
        P = {(rr, cc) for (r, c) in P for (rr, cc) in {(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)}} & M
        M -= P
    return home in P
