def any_arrows(arrows):
    return not all((ar.get('damaged', False) for ar in arrows))
