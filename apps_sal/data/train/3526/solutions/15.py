def any_arrows(arrows):
    return any((not x.get('damaged', False) for x in arrows))
