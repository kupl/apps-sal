def special(card):
    if card[0] == 'A':
        return 4
    if card[0] == 'K':
        return 3
    if card[0] == 'Q':
        return 2
    if card[0] == 'J':
        return 1
    return 0


def who_wins_beggar_thy_neighbour(player1, player2):
    common = []
    move = 1
    game = True
    cards = 0
    while cards < 10000:
        while not common or not special(common[-1]):
            if move == 1:
                if not player1:
                    return 1
                common.append(player1.pop(0))
                cards += 1
                move = 2
            else:
                if not player2:
                    return 0
                common.append(player2.pop(0))
                cards += 1
                move = 1
        penalty = special(common[-1])
        while penalty:
            if move == 1:
                if not player1:
                    return 1
                common.append(player1.pop(0))
                cards += 1
                if not special(common[-1]):
                    penalty -= 1
                if special(common[-1]):
                    penalty = special(common[-1])
                    move = 2
            else:
                if not player2:
                    return 0
                common.append(player2.pop(0))
                cards += 1
                if not special(common[-1]):
                    penalty -= 1
                if special(common[-1]):
                    penalty = special(common[-1])
                    move = 1
        if move == 1:
            player2.extend(common)
            common = []
            move = 2
        else:
            player1.extend(common)
            common = []
            move = 1
    return None
