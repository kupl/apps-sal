from collections import defaultdict


def mouse_path(s):
    # use the shoelace method to calculate area from coordinates

    # direction given as a tuple on coordinae plane, eg (1,0) right

    # set direction based on current direction and turn direction
    turns = {direction: defaultdict(tuple) for direction in ((0, 1), (0, -1), (-1, 0), (1, 0))}
    turns[(0, -1)]['L'], turns[(0, -1)]['R'] = turns[(0, 1)]['R'], turns[(0, 1)]['L'] = (1, 0), (-1, 0)  # dx,dy
    turns[(-1, 0)]['L'], turns[(-1, 0)]['R'] = turns[(1, 0)]['R'], turns[(1, 0)]['L'] = (0, -1), (0, 1)  # dx,dy

    coords = [(0, 0)]

    # first we need to parse the string for coordinates, assume an initial direction of right
    num = []
    x = y = 0
    direction = (1, 0)

    for a in s + ' ':
        if a.isdigit():
            num.append(a)
        else:
            num = int(''.join(num))
            x += num * direction[0]
            y += num * direction[1]
            coords.append((x, y))
            direction = turns[direction][a]
            num = []

    # check if the shape is not closed
    if coords[0] != coords[-1]:
        return None
    # check if we don't end in a corner (even number of coordinates, try drawing out and you will see)
    if len(coords) % 2 == 0:
        return None

    # check for intersections, check each horizonal line with each vertical line (excluding the ones beginning and
    # ending at the ends of the horizonal line) for intersections. A line is paramterized by two coordinates, its start and
    # end point. if there are more than 2 vertical lines intersecting horizonal, return None
    horizontals = [(coords[i], coords[i + 1]) for i in range(0, len(coords) - 1, 2)]
    verticals = [(coords[i], coords[i + 1]) for i in range(1, len(coords) - 1, 2)]

    for (x1, y1), (x2, y2) in horizontals:
        max_x, min_x = max(x1, x2), min(x1, x2)
        count = 0
        for (a1, b1), (a2, b2) in verticals:
            max_y, min_y = max(b1, b2), min(b1, b2)
            if min_x <= a1 <= max_x and min_y <= y1 <= max_y:
                count += 1
                if count > 2:
                    return None

    # main shoelace formula
    area = 0
    j = 0
    for i in range(1, len(coords)):
        area += (coords[j][0] + coords[i][0]) * (coords[j][1] - coords[i][1])
        j = i

    return abs(area / 2)
