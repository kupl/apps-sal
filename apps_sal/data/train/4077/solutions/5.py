def premier_league_standings(teams):
    if len(teams) == 1:
        return teams
    next_season = []
    for (key, value) in list(teams.items()):
        if key != 1:
            next_season.append(value)
    sorted_nex = sorted(next_season)
    sorted_dict = {}
    for (key, value) in enumerate(sorted_nex, 2):
        sorted_dict[1] = teams[1]
        sorted_dict[key] = value
    return sorted_dict
