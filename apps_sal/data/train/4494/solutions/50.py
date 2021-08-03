def points(games):
    points_res = 0
    for res_str in games:
        x = int(res_str[0])
        y = int(res_str[2])
        if x > y:
            points_res += 3
        elif x == y:
            points_res += 1
    return points_res
