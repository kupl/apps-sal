def any_arrows(arrows):
    return any([x for x in arrows if x.get('damaged') == False or x.get('damaged') == None])
