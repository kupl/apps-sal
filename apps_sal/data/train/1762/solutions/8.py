class point():
    def __init__(self, x, y):
        self.x, self.y = x, y
    __str__ = lambda self: f"{self.x}, {self.y}"
    __add__ = lambda self, p2: point(self.x + p2.x, self.y + p2.y)
    __mul__ = lambda self, num: point(self.x * num, self.y * num)
    __eq__  = lambda self, p2: True if self.x == p2.x and self.y == p2.y else False

def turn_to_dir(c_dir, turn):
    return point(-c_dir.y, c_dir.x) if turn == 'L' else point(c_dir.y, -c_dir.x)

def str_to_points(string):
    last_index = 0
    direction = point(1,0)
    points = [point(0,0)]
    for index, symbol in enumerate(string + 'L'):
        if symbol in 'LR':
            points.append(points[-1] + direction * int(string[last_index:index]))
            direction = turn_to_dir(direction, symbol)
            last_index = index + 1
    return points

def doIntersect(seg1, seg2):
    # seg1 = [(p0_x, p0_y), (p1_x, p1_y)]
    # seg2 = [(p2_x, p2_y), (p3_x, p3_y)]
    p0_x = seg1[0].x
    p0_y = seg1[0].y
    p1_x = seg1[1].x
    p1_y = seg1[1].y
    p2_x = seg2[0].x
    p2_y = seg2[0].y
    p3_x = seg2[1].x
    p3_y = seg2[1].y

    s1_x = p1_x - p0_x
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x
    s2_y = p3_y - p2_y

    denom = -s2_x * s1_y + s1_x * s2_y

    s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / denom if denom != 0 else -1
    t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / denom if denom != 0 else -1

    if 0 <= s <= 1 and 0 <= t <= 1:
        return True

def check(points):
    # the path doesn't complete the loop back to the mousehole
    if points[0] != points[-1]:
        return False
    # the mousehole is located along the straight path of a wall
    if points[1].x == points[-2].x or points[1].y == points[-2].y:
        return False
    # the path intersects/overlaps itself
    points_count = len(points) - 1
    for i in range(points_count - 3):
        for j in range(i+2, points_count - 1):
            if doIntersect((points[i], points[i+1]), (points[j], points[j+1])):
                return False
    for i in range(1, points_count - 2):
        # print((str(points[0]), str(points[-2])), (str(points[i]), str(points[i+1])))
        if doIntersect((points[0], points[-2]), (points[i], points[i+1])):
            return False
    return True

def area(p):
    return 0.5 * abs(sum(segment[0].x*segment[1].y - segment[1].x*segment[0].y
                         for segment in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])

def mouse_path(s):
    points = str_to_points(s)
    return area(points) if check(points) else None
