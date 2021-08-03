def premier_league_standings(teams):
    order = [teams[1]] + sorted(team for place, team in teams.items() if place != 1)
    return {place: team for place, team in enumerate(order, 1)}
