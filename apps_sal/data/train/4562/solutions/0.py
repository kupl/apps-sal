def round(flash_pile, turtle_pile):
    faceup_pile = []
    while turtle_pile:
        for pile in flash_pile, turtle_pile:
            faceup_pile.append(pile.pop(0))
            if len(faceup_pile) >= 2 and faceup_pile[-1] == faceup_pile[-2]:
                flash_pile.extend(faceup_pile)
                return True

def snap(flash_pile, turtle_pile):
    for i in range(26):
        if not round(flash_pile, turtle_pile):
            return i
