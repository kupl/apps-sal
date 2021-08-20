def men_still_standing(cards):
    (players, Y, R) = ({'A': 11, 'B': 11}, set(), set())
    for c in cards:
        if c[:-1] not in R:
            players[c[0]] -= c[-1] == 'R' or c[:-1] in Y
        if 6 in players.values():
            break
        (R if c[-1] == 'R' or c[:-1] in Y else Y).add(c[:-1])
    return (players['A'], players['B'])
