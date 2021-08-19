def robot_walk(ds):
    (xs, ys) = ({0}, {0})
    (x, y) = (0, 0)
    (dx, dy) = (0, 1)
    for d in ds:
        (x, y) = (x + d * dx, y + d * dy)
        xs.add(x)
        ys.add(y)
        (dx, dy) = (-dy, dx)
    (x, y) = (0, 0)
    (dx, dy) = (0, 1)
    visited = {(0, 0)}
    for d in ds:
        (x1, y1) = (x + d * dx, y + d * dy)
        ((bx, by), (ex, ey)) = sorted(((x + dx, y + dy), (x1, y1)))
        if dy == 0:
            for cx in xs:
                if bx <= cx <= ex and (cx, y) in visited:
                    return True
                visited.add((cx, y))
        else:
            for cy in ys:
                if by <= cy <= ey and (x, cy) in visited:
                    return True
                visited.add((x, cy))
        (x, y) = (x1, y1)
        (dx, dy) = (-dy, dx)
    return False
