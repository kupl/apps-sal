def euclidean_distance(cell, goal):
    dx = abs(cell[0] - goal[0])
    dy = abs(cell[1] - goal[1])
    return (dx**2 + dy**2)**.5


def peaceful_yard(yard, min_distance):
    coord = []
    for x in range(len(yard)):
        for y in range(len(yard[x])):
            if yard[x][y] in {'L', 'R', 'M'}:
                if any(euclidean_distance(cat_pos, (x, y)) < min_distance for cat_pos in coord):
                    return False
                coord.append((x, y))
    return True
