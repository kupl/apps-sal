def edge_detection(image):
    image = [int(v) for v in image.split(' ')]
    width = image[0]
    (map, line, flat) = ([], [], [])
    (rest, f) = (width, 1)
    (current, result) = (['', width], [''])

    def apply(value):
        if current[0] == value:
            current[1] += 1
        else:
            result[0] += ' ' + str(current[0]) + ' ' + str(current[1])
            current[0] = value
            current[1] = 1

    def diff(R, C, r, c):
        r += R
        c += C
        return abs(flat[R][C] - flat[r][c]) if 0 <= r < len(flat) and 0 <= c < width else 0
    while f < len(image):
        line.append([image[f], min(rest, image[1 + f])])
        if image[1 + f] < rest:
            rest -= image[1 + f]
            f += 2
        else:
            image[1 + f] -= rest
            if image[1 + f] < 3 * width:
                if image[1 + f] < 1:
                    f += 2
                map.append(line)
                line = []
                rest = width
            else:
                map.append(line)
                map.append([[image[f], width]])
                map.append([[image[f], width, image[1 + f] // width - 2]])
                map.append([[image[f], width]])
                line = []
                image[1 + f] %= width
                rest = width - image[1 + f]
                if image[1 + f]:
                    line.append(image[f:2 + f])
                f += 2
    for v in map:
        t = f = 0
        line = []
        flat.append(line)
        for _ in range(width):
            line.append(v[f][0])
            t += 1
            if v[f][1] <= t:
                (t, f) = (0, 1 + f)
    for (r, row) in enumerate(map):
        if 2 < len(row[0]):
            apply(0)
            current[1] += width * row[0][2] - 1
        else:
            for f in range(width):
                apply(max(diff(r, f, -1, 0), diff(r, f, -1, 1), diff(r, f, 0, 1), diff(r, f, 1, 1), diff(r, f, 1, 0), diff(r, f, 1, -1), diff(r, f, 0, -1), diff(r, f, -1, -1)))
    apply(None)
    return result[0][2:]
