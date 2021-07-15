def any_arrows(arrows):
    return any((x.get('damaged', None) == None or x['damaged'] == False) for x in arrows)
