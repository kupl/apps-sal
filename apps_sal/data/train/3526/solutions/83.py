def any_arrows(arrows):
    return False if all([i.get('damaged', False) for i in arrows]) else True
