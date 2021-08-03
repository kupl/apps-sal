def who_wins_beggar_thy_neighbour(hand_1, hand_2):
    hs, vs = (hand_1, hand_2), {'J': 1, 'Q': 2, 'K': 3, 'A': 4}
    hands = {player: [vs.get(card[0], 0) for card in hs[player]] for player in range(2)}
    # print(hands)
    player = 0
    draw = -1
    pile = []
    while hands[player]:
        pile.append(hands[player].pop(0))
        draw -= 1

        if pile[-1] > 0:
            draw = pile[-1]
            player = 1 - player
            continue

        if draw == 0:
            player = 1 - player
            hands[player].extend(pile)
            pile = []
            draw = -1
            continue

        if draw < 0:
            player = 1 - player

    return 1 - player
