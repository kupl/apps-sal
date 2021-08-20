def points(games):
    point = 0
    for i in games:
        b = i.split(':')
        if int(b[0]) > int(b[1]):
            point += 3
        elif int(b[0]) < int(b[1]):
            point += 0
        elif int(b[0]) == int(b[1]):
            point += 1
    return point
