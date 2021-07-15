def points(games):
    total_pts = 0

    for game in games:
        x, y = game.split(":")
        if x == y:
            total_pts += 1
        elif x > y:
            total_pts += 3
    
    return total_pts

