import re


def path_to_point(path, r=[-1, 0], position=[0, 0]):
    rotations = {'L': lambda a, b: (b * -1, a), 'R': lambda a, b: (b, a * -1)}
    result = []
    for v in re.findall(r'\d+|.', path):
        if v.isnumeric():
            position = position[0] + r[0] * int(v), position[1] + r[1] * int(v)
            result.append(position)
        else:
            r = rotations[v](*r)
    return result


def check_path(points):
    print(points)
    if len(points) % 2 != 0 or points[-1] != (0, 0) or (
       len(points) != len(set(points))):
        return False

    vertical_segments, horizontal_segments = [], []
    for i in range(0, len(points), 2):
        p1, p2, p3 = points[i], points[i + 1], points[(i + 2) % len(points)]
        v = (p1, p2)
        h = (p2, p3)
        for s in vertical_segments:
            if min(s[0][1], s[1][1]) <= h[0][1] <= max(s[0][1], s[1][1]) and (
               min(h[0][0], h[1][0]) <= s[0][0] <= max(h[0][0], h[1][0]) and not
               (h[0] == s[0] or h[0] == s[1] or h[1] == s[0] or h[1] == s[1])):
                return False

        for s in horizontal_segments:
            if min(s[0][0], s[1][0]) <= v[0][0] <= max(s[0][0], s[1][0]) and (
               min(v[0][1], v[1][1]) <= s[0][1] <= max(v[0][1], v[1][1]) and not
               (v[0] == s[0] or v[0] == s[1] or v[1] == s[0] or v[1] == s[1])):
                return False

        vertical_segments.append(v)
        horizontal_segments.append(h)

    return True


def mouse_path(s):
    points = path_to_point(s)
    if not check_path(points):
        return None

    separators = sorted(list(set([p[1] for p in points])))

    _points = []
    for i in range(len(points)):
        p1, p2 = points[i], points[(i+1) % len(points)]
        _points.append(p1)
        if p1[0] == p2[0]:
            for j in (separators if p1[1] < p2[1] else separators[::-1]):
                if min(p1[1], p2[1]) < j < max(p1[1], p2[1]):
                    _points.append((p1[0], j))
    points = _points

    result = 0
    separators = list(separators)
    for i in range(len(separators) - 1):
        y1, y2 = separators[i], separators[i + 1]
        temp = []
        for p in sorted(list(filter(lambda x: x[1] == separators[i], points)))[::-1]:
            j = points.index(p)
            if points[j - 1] == (p[0], y2) or points[(j + 1) % len(points)] == (p[0], y2):
                temp.append(p)
        if len(temp) % 2 != 0:
            return None
        for j in range(0, len(temp), 2):
            result += (y2 - y1) * (temp[j][0] - temp[j + 1][0])
    return result
