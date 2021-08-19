def premier_league_standings(teams):
    dct = {1: teams[1]}
    dct.update({i: t for (i, t) in enumerate(sorted(set(teams.values()) - {teams[1]}), 2)})
    return dct
