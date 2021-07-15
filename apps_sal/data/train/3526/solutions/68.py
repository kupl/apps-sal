def any_arrows(arrows):
    goodArrows = False
    for a in arrows:
        goodArrows = goodArrows or not a.get('damaged')    
    return goodArrows
