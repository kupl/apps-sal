def snap(flash, turtle):
    snaps = 0
    pile = []
    players = (flash, turtle)
    i = [0, 0]
    p = 0
    while i[1] < len(turtle):
        card = players[p][i[p]]
        i[p] += 1
        if pile and card == pile[-1]:
            flash.extend(pile)
            flash.append(card)
            snaps += 1
            pile = []
            p = 0
        else:
            pile.append(card)
            p ^= 1
    return snaps
