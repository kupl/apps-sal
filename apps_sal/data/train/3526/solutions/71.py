def any_arrows(arrows):
    return len([a for a in arrows if not a.get('damaged', False)]) != 0
