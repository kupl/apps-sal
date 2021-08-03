def premier_league_standings(teams):
    return {c: n for c, (_, n) in enumerate(sorted(teams.items(), key=lambda t: (t[0] > 1, t[1])), 1)}
