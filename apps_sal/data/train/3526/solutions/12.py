def any_arrows(arrows):
    return any(not a.get('damaged', False) for a in arrows)
