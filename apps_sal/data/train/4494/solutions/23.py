def points(games):
    count = 0
    for i in games:
        if int(i[0]) > int(i[2]):
            count += 3
        elif int(i[0]) == int(i[2]):
            count += 1
    return count
