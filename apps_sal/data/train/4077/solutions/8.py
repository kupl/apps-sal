def premier_league_standings(teams):
    lst = [(x, y) for (x, y) in teams.items()]
    lst = [y for (x, y) in lst if x == 1] + sorted([y for (x, y) in lst if x != 1])
    return {i: y for (i, y) in enumerate(lst, 1)}
