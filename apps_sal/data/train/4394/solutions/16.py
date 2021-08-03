def men_still_standing(cards):
    team_a = {i + 1: 0 for i in range(11)}
    team_b = team_a.copy()
    teams_dict = {'A': team_a, 'B': team_b}
    gone_players = {'A': [], 'B': []}
    for booking in cards:
        team = teams_dict[booking[0]]
        player = int(booking[1:-1])
        if player in gone_players[booking[0]]:
            continue
        if booking[-1] == 'R':
            team[player] += 1
        else:
            team[player] += 0.5
        if team[player] >= 1:
            gone_players[booking[0]].append(player)
        if len(gone_players[booking[0]]) > 4:
            break
    return tuple([11 - len(gone_players['A']), 11 - len(gone_players['B'])])
