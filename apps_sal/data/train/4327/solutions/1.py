def chameleon(chameleons, desiredColor):

    color_count = dict(list(zip(['r', 'g', 'b'], chameleons)))
    target = ['r', 'g', 'b'][desiredColor]
    other_color = [i for i in ['r', 'g', 'b'] if i != target]
    to_meet = sorted([(k, color_count[k]) for k in other_color], key=lambda x: x[1])

    if to_meet[0][1] == to_meet[1][1]:
        return to_meet[0][1]
    meets = to_meet[0][1]
    meet_left = to_meet[1][1] - meets
    color_count[target] += to_meet[0][1]
    # print meet_left, meets
    if meet_left % 3 != 0 or color_count[target] == 0:

        return -1
    return meets + meet_left
