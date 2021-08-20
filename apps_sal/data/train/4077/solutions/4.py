def premier_league_standings(teams):
    new = [teams[1]] + sorted((teams[n] for n in range(2, len(teams) + 1)))
    return {i: team for (i, team) in enumerate(new, 1)}
