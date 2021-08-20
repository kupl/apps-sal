def men_still_standing(cards):
    teams = {'A': [True, True, True, True, True, True, True, True, True, True, True], 'B': [True, True, True, True, True, True, True, True, True, True, True]}
    for card in cards:
        team = card[0]
        color = card[-1]
        player = int(card[1:-1]) - 1
        if color == 'R' or teams[team][player] == 'Y':
            teams[team][player] = False
        elif color == 'Y' and teams[team][player] != False:
            teams[team][player] = 'Y'
        if len([1 for (_, team) in list(teams.items()) if players_up(team) >= 7]) < 2:
            break
    return (players_up(teams['A']), players_up(teams['B']))


def players_up(players):
    return len([1 for player in players if player != False])
