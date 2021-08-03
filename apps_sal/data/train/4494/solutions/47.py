def points(games):

    g = 0

    for i in games:

        j = i.split(':')

        if j[0] > j[1]:
            g += 3

        elif j[0] == j[1]:
            g += 1

    return g
