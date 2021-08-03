def snap(flash_pile, turtle_pile):
    centre_pile = []
    i = 0
    while turtle_pile:
        card = turtle_pile.pop(0) if i % 2 else flash_pile.pop(0)
        centre_pile.append(card)
        if i > 0 and centre_pile[-2] == centre_pile[-1]:
            return 1 + snap(flash_pile + centre_pile, turtle_pile)
        i += 1
    return 0
