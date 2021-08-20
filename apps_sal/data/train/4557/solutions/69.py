def row_weights(array):
    team_sec = []
    team_frst = []
    for (index, item) in enumerate(array):
        if index % 2 == 0:
            team_frst.append(item)
        else:
            team_sec.append(item)
    return (sum(team_frst), sum(team_sec))
