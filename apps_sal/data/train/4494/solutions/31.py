def points(games):

    final = 0
    for score in games:
        x, y = score.split(":")
        if x > y:
            final += 3
        elif x == y:
            final += 1
        else:
            final + 0

    return final
