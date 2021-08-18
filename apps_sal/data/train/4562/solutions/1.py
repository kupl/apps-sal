def snap(flash_pile, turtle_pile):
    middle_pile = []
    snap = 0
    while turtle_pile != []:

        middle_pile.append(flash_pile.pop(0))
        if len(middle_pile) > 1 and middle_pile[-2] == middle_pile[-1]:
            snap += 1
            flash_pile.extend(middle_pile)
            middle_pile = []
            continue

        middle_pile.append(turtle_pile.pop(0))
        if len(middle_pile) > 1 and middle_pile[-2] == middle_pile[-1]:
            snap += 1
            flash_pile.extend(middle_pile)
            middle_pile = []

    return snap
