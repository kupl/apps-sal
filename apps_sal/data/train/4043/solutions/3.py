from itertools import combinations


def calc(gamemap):
    x_max, y_max = len(gamemap) - 1, len(gamemap[0]) - 1
    last_step = x_max + y_max - 1
    best_paths = {((0, 1), (1, 0)): gamemap[0][0] + gamemap[0][1] + gamemap[1][0] + gamemap[-2][-1] + gamemap[-1][-2] + gamemap[-1][-1]}
    for step in range(2, last_step):
        new_best_paths, x_lower_limit, x_upper_limit = {}, max(0, step - y_max), min(step, x_max)
        for x1, x2 in combinations(range(x_lower_limit, x_upper_limit + 1), 2):
            y1, y2 = step - x1, step - x2
            previous_steps = set(((_x1, _y1), (_x2, _y2)) for _x1, _y1 in ((x1 - 1, y1), (x1, y1 - 1)) for _x2, _y2 in ((x2 - 1, y2), (x2, y2 - 1)))
            best_path_value = max([best_paths[points] for points in previous_steps if points in best_paths])
            new_best_paths[((x1, y1), (x2, y2))] = gamemap[x1][y1] + gamemap[x2][y2] + best_path_value
        best_paths = new_best_paths
    return max(best_paths.values())
