def any_arrows(arrows):
    return any((not a.get('damaged') for a in arrows))
