def points(games):
    points = 0
    
    for game in games:
        point = list(map(int, game.split(":")))
        if point[0] > point[1]:
            points += 3
        elif point[0] == point[1]:
            points += 1

    return points

