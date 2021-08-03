import math


def web_length(delta_x, height):
    return math.sqrt(delta_x**2 + (height - 50)**2)


def score(distance, delta_x, height):
    return distance / math.sqrt(delta_x**2 + (height - 50)**2)


def select_next_latch(cur_pos, buildings):

    potiential_latch = []
    for bd in buildings:
        x_lower_bound = max(bd[0], cur_pos)
        delta_x_upper_bound = min(math.floor(math.sqrt(bd[2] * 60 - 2100)), bd[1] - cur_pos)
        if x_lower_bound <= cur_pos + delta_x_upper_bound:
            potiential_latch.append([x_lower_bound, cur_pos + delta_x_upper_bound, bd[2]])

    # latch loc, score, height
    common_best = [cur_pos, 0, 0]
    special_best = [-1, 0, 0]
    for bd in potiential_latch:
        for x in range(bd[0], bd[1] + 1):
            if cur_pos + 2 * (x - cur_pos) >= buildings[-1][1]:
                cur_score = score(buildings[-1][1] - cur_pos, x - cur_pos, bd[2])
                if cur_score >= special_best[1]:
                    special_best = [x, cur_score, bd[2]]
            else:
                cur_score = score(2 * (x - cur_pos), x - cur_pos, bd[2])

            if cur_score >= common_best[1]:
                common_best = [x, cur_score, bd[2]]

    return common_best, special_best


def search(cur_pos, end_pos, buildings):

    if cur_pos >= end_pos:
        return 0, []

    cb, sb = select_next_latch(cur_pos, buildings)

    last_r = web_length(sb[0] - cur_pos, sb[2])
    best_r = web_length(cb[0] - cur_pos, cb[2])

    min_lenth, latch_list = search(cur_pos + 2 * (cb[0] - cur_pos), end_pos, buildings)

    if sb[0] == -1 or sb[0] == cb[0]:
        return min_lenth + best_r, [cb[0]] + latch_list
    else:
        if min_lenth + best_r > last_r:
            return last_r, [sb[0]]
        else:
            return min_lenth + best_r, [cb[0]] + latch_list


def spidey_swings(ar):

    buildings = []
    start_pos = 0
    for b in ar:
        buildings.append([start_pos, start_pos + b[1], b[0]])
        start_pos += b[1]

    cur_pos = 0
    latch_points = []
    while(cur_pos < buildings[-1][1]):
        cb, sb = select_next_latch(cur_pos, buildings)

        if sb[0] == -1 or sb[0] == cb[0]:
            latch_points.append(cb[0])
            cur_pos += (cb[0] - cur_pos) * 2
        else:
            _, final_points = search(cur_pos, buildings[-1][1], buildings)
            latch_points += final_points
            cur_pos += (sb[0] - cur_pos) * 2

    return latch_points
