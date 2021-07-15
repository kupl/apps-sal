def men_still_standing(cards):
    teams = {'A': dict.fromkeys(range(1, 12), 2), 'B': dict.fromkeys(range(1, 12), 2)}
    for card in cards:
        t, number, color = card[:1], int(card[1:-1]), card[-1:]
        team = teams[t]
        if number not in team:
            continue
        team[number] -= 2 if color == 'R' else 1
        if team[number] <= 0:
            del team[number]
            if len(team) < 7:
                break
    return len(teams['A']), len(teams['B'])
