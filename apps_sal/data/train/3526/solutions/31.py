def any_arrows(arrows):
    all_bools = []
    if len(arrows) < 1:
        return False
    for i in arrows:
        if i.get('range', 0) >= 0 and i.get('damaged', False) == False:
            all_bools.append(True)
        if i.get('range', 0) >= 0 and i.get('damaged') == True:
            all_bools.append(False)
    if True in all_bools:
        return True
    else:
        return False
