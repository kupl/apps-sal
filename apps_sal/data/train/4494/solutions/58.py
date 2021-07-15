def points(games):
    points = 0
    for game in games:
        score = game.split(':')
        if score[0] > score[1]:
            points += 3
        elif score[0] == score[1]:
            points += 1
    return points
