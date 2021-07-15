def points(games):
    points = 0
    for each_str in games:
        x = int(each_str[0])
        y = int(each_str[2])
        if x > y:
            points += 3
        elif x == y:
            points += 1
    return points
