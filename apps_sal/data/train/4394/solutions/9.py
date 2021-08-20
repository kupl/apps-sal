def men_still_standing(cards):
    players = [[2] * 11, [2] * 11]
    AB = {'A': 0, 'B': 1}
    penalty = {'Y': 1, 'R': 2}
    for card in cards:
        (team, number, color) = (card[0], int(card[1:-1]), card[-1])
        players[AB[team]][number - 1] -= penalty[color]
        if sum((i > 0 for i in players[AB[team]])) < 7:
            break
    return tuple((sum((i > 0 for i in x)) for x in players))
