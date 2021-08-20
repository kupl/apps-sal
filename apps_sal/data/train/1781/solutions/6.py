from collections import deque


def who_wins_beggar_thy_neighbour(*hands):
    special = {c: i + 1 for (i, c) in enumerate('JQKA')}
    hands = [deque((c[0] for c in h)) for h in hands]
    pile = []
    (player, penalty) = (0, 0)
    while hands[player]:
        pile.append(hands[player].popleft())
        penalty -= 1
        if penalty == 0 and (not pile[-1] in special):
            hands[player ^ 1].extend(pile)
            pile = []
        if penalty < 1 or pile[-1] in special:
            player ^= 1
            penalty = special.get(pile[-1], 0) if pile else 0
    return player ^ 1
