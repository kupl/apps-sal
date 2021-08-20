def men_still_standing(cards):
    A = {k: 0 for k in range(1, 12)}
    B = A.copy()
    for card in cards:
        team = A if card[0] == 'A' else B
        player = int(card[1:-1])
        color = card[-1]
        if player not in team:
            continue
        team[player] += 1 if color == 'Y' else 2
        if team[player] >= 2:
            del team[player]
        if len(team) < 7:
            break
    return (len(A), len(B))
