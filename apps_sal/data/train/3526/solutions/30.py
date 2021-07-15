def any_arrows(arrows):
    return any(True for x in arrows if not x.get('damaged'))
