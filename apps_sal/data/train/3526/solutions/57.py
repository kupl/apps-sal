def any_arrows(arrows):
    for a in arrows:
        if 'damaged' not in list(a.keys()):
            return True
        if a['damaged'] == False:
            return True
    return False
