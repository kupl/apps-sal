def points(games):
    sumx = 0
    for x in games:
        temp = x.split(':')
        if temp[0] == temp[1]:
            sumx += 1
        elif temp[0] > temp[1]:
            sumx += 3
    return sumx
