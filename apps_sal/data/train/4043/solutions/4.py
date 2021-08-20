from itertools import combinations


def calc(gamemap):
    (x_max, y_max) = (len(gamemap) - 1, len(gamemap[0]) - 1)
    last_step = x_max + y_max - 1
    dynamic_table = {((0, 1), (1, 0)): gamemap[0][0] + gamemap[0][1] + gamemap[1][0] + gamemap[-2][-1] + gamemap[-1][-2] + gamemap[-1][-1]}
    for step in range(2, last_step):
        _dynamic_table = {}
        x_lower_limit = max(0, step - y_max)
        x_upper_limit = min(step + 1, x_max + 1)
        for (x1, x2) in combinations(range(x_lower_limit, x_upper_limit), 2):
            (y1, y2) = (step - x1, step - x2)
            previous_steps = set()
            d1 = []
            if x1:
                d1.append((-1, 0))
            if y1:
                d1.append((0, -1))
            d2 = []
            if x2:
                d2.append((-1, 0))
            if y2:
                d2.append((0, -1))
            for (_dx1, _dy1) in d1:
                for (_dx2, _dy2) in d2:
                    (_x1, _y1) = (x1 + _dx1, y1 + _dy1)
                    (_x2, _y2) = (x2 + _dx2, y2 + _dy2)
                    if _x1 != _x2:
                        previous_steps.add(((_x1, _y1), (_x2, _y2)))
            best_path_value = max([dynamic_table[points] for points in previous_steps])
            _dynamic_table[(x1, y1), (x2, y2)] = gamemap[x1][y1] + gamemap[x2][y2] + best_path_value
        dynamic_table = _dynamic_table
    return max(dynamic_table.values())
