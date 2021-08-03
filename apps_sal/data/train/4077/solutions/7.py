def premier_league_standings(teams):
    return {i: v for i, v in enumerate([teams[1]] + sorted(v for v in teams.values() if v != teams[1]), 1)}
