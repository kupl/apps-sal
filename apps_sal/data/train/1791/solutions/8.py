def escape(maze):
    h, w = len(maze), len(maze[0])
    maze = [list(row) for row in maze]
    i, j, face = find_self(maze)
    maze[i][j] = '
    paths = [[i, j, face, []]]
    while paths:
        i, j, face, path = paths.pop(0)
        if i == 0 or i + 1 == h or j == 0 or j + 1 == w:
            return path
        for step, mi, mj, new_face in directions(i, j, face):
            if maze[mi][mj] != '
            paths.append([mi, mj, new_face, path + step])
            maze[mi][mj] = '
    return []


def find_self(maze):
    faces = {'^': (-1, 0), '<': (0, -1), 'v': (1, 0), '>': (0, 1)}
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell in faces:
                return i, j, faces[cell]


def directions(i, j, face):
    fi, fj = face
    return [[['F'], i + fi, j + fj, face],
            [['L', 'F'], i - fj, j + fi, (-fj, fi)],
            [['R', 'F'], i + fj, j - fi, (fj, -fi)],
            [['B', 'F'], i - fi, j - fj, (-fi, -fj)]]
