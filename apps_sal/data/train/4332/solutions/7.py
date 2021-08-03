def langtons_ant(n):
    grid = [[0]]
    column = 0
    row = 0
    direction = 0
    move = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1),
    }
    rows = len(grid)
    cols = len(grid[0])
    ap = (row, column)
    dir = direction
    n_black = 0

    max_simple_range = 11000
    n_black_highway_ref = []
    ref = 0

    for i in range(1, n + 1):
        if (grid[ap[0]][ap[1]]) == 1:
            grid[ap[0]][ap[1]] = 0
            dir = (dir + 1) % 4
            n_black -= 1
        else:
            grid[ap[0]][ap[1]] = 1
            dir = (dir - 1) % 4
            n_black += 1
        ap = (ap[0] + move[dir][0], ap[1] + move[dir][1])

        if ap[0] >= rows:
            grid = grid + ([[0] * cols])
            rows += 1
        elif ap[0] < 0:
            grid = ([[0] * cols]) + grid
            rows += 1
            ap = (0, ap[1])

        if ap[1] >= cols:
            for j, r in enumerate(grid):
                grid[j] = r + [0]
            cols += 1
        elif ap[1] < 0:
            for j, r in enumerate(grid):
                grid[j] = [0] + r
            cols += 1

            ap = (ap[0], 0)

        if i >= max_simple_range:
            if i == max_simple_range:
                ref = n_black
            n_black_highway_ref.append(n_black - ref)

            if i == (max_simple_range + 104):
                break

    if n > (max_simple_range + 104):
        n_black += (n_black_highway_ref[-1] * (((n - max_simple_range) // 104) - 1))
        n_black += (n_black_highway_ref[((n - max_simple_range) % 104)])
    return n_black
