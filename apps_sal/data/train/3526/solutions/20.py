def any_arrows(arrows):
    return not all((a.get('damaged', False) for a in arrows))
