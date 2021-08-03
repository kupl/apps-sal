def premier_league_standings(teams):
    return {i: team[1] for i, team in enumerate(sorted(teams.items(), key=lambda x: (x[0] != 1, x[1])), 1)}
