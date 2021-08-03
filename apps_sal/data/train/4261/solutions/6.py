from itertools import cycle


def robot_walk(arr):
    directions, li, m, n = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)]), [], 0, 0
    for i in arr:
        k, l = next(directions)
        li.append([[m, n], [m + k * i, n + l * i]])
        m += k * i
        n += l * i
        test = li[-1]
        for o, p in li[:-3]:
            same, same1 = not o[0] == p[0], not test[0][0] == test[1][0]
            if same != same1:
                temp, temp1 = sorted([o[same ^ 1], p[same ^ 1]]), sorted([test[0][same1 ^ 1], test[1][same1 ^ 1]])
                if o[same] >= temp1[0] and o[same] <= temp1[1] and test[0][same1] >= temp[0] and test[0][same1] <= temp[1]:
                    return True
    return False
