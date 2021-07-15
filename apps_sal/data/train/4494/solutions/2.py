def points(games):
    count = 0
    for match in games:
        x = match.split(":")
        if x[0] > x[1]:
            count += 3
        elif x[0] == x[1]:
            count += 1
    return count
