def any_arrows(arrows):
    return any(not x.get('damaged') for x in arrows)
