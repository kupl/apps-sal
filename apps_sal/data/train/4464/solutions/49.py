def feast(beast, dish):
    beastList = list(beast)
    dishList = list(dish)
    if beastList[0] == dishList[0] and beastList[-1] == dishList[-1]: 
        return True
    else: 
        return False
