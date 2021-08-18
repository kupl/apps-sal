def feast(beast, dish):
    pass
    indexBeast = len(beast)
    indexDish = len(dish)
    beast1 = beast[0]
    beastLast = beast[indexBeast - 1]
    dish1 = dish[0]
    dishLast = dish[indexDish - 1]

    if beast1 == dish1 and beastLast == dishLast:
        return True
    else:
        return False
