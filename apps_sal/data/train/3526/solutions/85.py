def any_arrows(arrows):
    return False in [i.get('damaged',False) for i in arrows]

