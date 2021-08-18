import math


def calc_web_length(current_loc, swing_point):
    x = swing_point[0] - current_loc[0]
    y = swing_point[1] - current_loc[1]
    x_travel = 2 * x
    web_length = math.sqrt(pow(x, 2) + pow(y, 2))
    bottom_height = swing_point[1] - web_length
    return x_travel, web_length, bottom_height


def spidey_swings(ar):
    buildings = ar

    latch_points = []
    prev_x = 0
    for building in buildings:
        for x in range(building[1] + 1):
            latch_points.append([x + prev_x, building[0]])
        prev_x += building[1]

    max_x = latch_points[-1][0]

    current_location = [0, 50]
    swing_list = []
    swing_end = None
    best_ratio = -999.0
    best_building = None

    while True:
        building = latch_points.pop(0)

        if building[0] <= current_location[0]:
            continue

        x_travel, length, height = calc_web_length(current_location, building)
        ratio = float(x_travel) / length

        if current_location[0] + x_travel >= max_x:
            best_ratio = ratio
            best_building = building
            for ltch_pt in latch_points[:20]:
                x_travel2, length2, height2 = calc_web_length(current_location, ltch_pt)
                swing_end2 = current_location[0] + x_travel2

                extra_x = swing_end2 - max_x
                x_travel2 -= extra_x
                ratio2 = float(x_travel2) / length2

                if ratio2 > best_ratio and height2 >= 20:
                    best_ratio = ratio2
                    best_building = ltch_pt

            swing_list.append(best_building[0])
            return swing_list

        if ratio > best_ratio and height >= 20.0:
            best_ratio = ratio
            best_building = building
            swing_end = current_location[0] + x_travel

        if height < 20.0:
            for ltch_pt in latch_points[:100]:
                x_travel2, length2, height2 = calc_web_length(current_location, ltch_pt)
                ratio2 = float(x_travel2) / length2
                swing_end2 = current_location[0] + x_travel2
                if swing_end2 >= max_x and height2 >= 20.0:
                    swing_list.append(ltch_pt[0])
                    return swing_list

            best_ratio = -999.0
            current_location[0] = swing_end
            swing_list.append(best_building[0])

    return swing_list
