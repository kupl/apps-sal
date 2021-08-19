def any_arrows(arrows):
    return False in [a.get('damaged', False) for a in arrows]
