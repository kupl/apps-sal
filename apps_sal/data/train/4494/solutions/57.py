def points(games):
    our_points = 0
    for game in games:
        if game[0] > game[2]:
            our_points = our_points + 3
        elif game[0] == game[2]:
            our_points = our_points + 1
        else:
            pass
    return our_points
