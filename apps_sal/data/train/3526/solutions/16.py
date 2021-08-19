def any_arrows(arrows):
    return sum((a.get('damaged', 0) for a in arrows)) < len(arrows)
