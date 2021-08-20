def robot_walk(a):
    if len(set(a)) == 1:
        return True
    movings = []
    p = (0, 0)
    dir = (0, 1)
    for k in a:
        new_p = (p[0] + k * dir[0], p[1] + k * dir[1])
        for (start, stop) in movings:
            if new_p[1] == p[1] and start[0] == stop[0] and (start[1] < new_p[1] <= stop[1] or start[1] > new_p[1] >= stop[1]) and (new_p[0] <= start[0] < p[0] or new_p[0] >= start[0] > p[0]):
                return True
            elif new_p[0] == p[0] and start[1] == stop[1] and (start[0] < new_p[0] <= stop[0] or start[0] > new_p[0] >= stop[0]) and (new_p[1] <= start[1] < p[1] or new_p[1] >= start[1] > p[1]):
                return True
        movings.append((p, new_p))
        p = new_p
        dir = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}[dir]
    return False
