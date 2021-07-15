def row_weights(array):
    team1 = []
    team2 = []
    e = 0
    if len(array) % 2 != 0 or len(array) == 1:
        array.append(0)
    for i in str(array):
        if e == len(array):
            break
        else:
            team2.append(array[e+1])
            team1.append(array[e])
            e += 2
    return sum(team1), sum(team2)

