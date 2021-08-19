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

    # replace the building X positions with cumulative distances and
    # ALL integer points along the way (inclusive)
    # swap the order while we're at it to get normal (x,y) points
    latch_points = []
    prev_x = 0
    for building in buildings:
        for x in range(building[1] + 1):
            latch_points.append([x + prev_x, building[0]])
        prev_x += building[1]

    # Record the final X position to be used for termination criteria
    max_x = latch_points[-1][0]

    # Loop Variables
    current_location = [0, 50]
    swing_list = []
    swing_end = None
    best_ratio = -999.0
    best_building = None

    while True:
        building = latch_points.pop(0)

        # Skip all latch points we may have passed during the swing
        if building[0] <= current_location[0]:
            continue

        # Calculate data for the current 'test' latch point
        x_travel, length, height = calc_web_length(current_location, building)
        ratio = float(x_travel) / length

        # Special check for end condition, this may be an non 'optimal' swing but
        # if it lands exactly on the final position, it is the final latch point
        if current_location[0] + x_travel >= max_x:
            best_ratio = ratio
            best_building = building
            for ltch_pt in latch_points[:20]:
                x_travel2, length2, height2 = calc_web_length(current_location, ltch_pt)
                swing_end2 = current_location[0] + x_travel2

                # Since this is at the end, we might over-travel, remove that extra
                # distance when calculating the web ratio
                extra_x = swing_end2 - max_x
                x_travel2 -= extra_x
                ratio2 = float(x_travel2) / length2

                if ratio2 > best_ratio and height2 >= 20:
                    best_ratio = ratio2
                    best_building = ltch_pt

            swing_list.append(best_building[0])
            return swing_list

        # Basic check: the point is good, check if it's better than any previous latch point
        if ratio > best_ratio and height >= 20.0:
            best_ratio = ratio
            best_building = building
            swing_end = current_location[0] + x_travel

        # End check: if this point goes negative, all further ones will too, so use the best
        # point up to here as the latch point and move current
        if height < 20.0:
            # just to be sure there aren't any better results, peak ahead for the next 50
            # latch points to see if one is better
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
