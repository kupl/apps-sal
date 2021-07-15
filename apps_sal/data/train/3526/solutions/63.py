def any_arrows(arrows):
    dam = 0
    for i in arrows:
        if 'damaged' in i:
            if i['damaged'] == True:
                dam += 1
    return dam < len(arrows)
