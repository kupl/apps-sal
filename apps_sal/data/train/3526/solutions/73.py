def any_arrows(arrows):
    return False in [arrow.get('damaged', False) for arrow in arrows]
