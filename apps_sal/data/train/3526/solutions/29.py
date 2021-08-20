def any_arrows(arrows):
    damaged_test = [bundle.get('damaged') for bundle in arrows]
    return None in damaged_test or False in damaged_test
