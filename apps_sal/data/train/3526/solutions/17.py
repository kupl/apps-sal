def any_arrows(arrows):
    return True in [arrow.get('damaged') != True for arrow in arrows]
