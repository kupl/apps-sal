def any_arrows(arrows):
    return any((not ar.get('damaged', False) for ar in arrows))
