def any_arrows(arrows):
    return any(['damaged' not in a or not a['damaged'] for a in arrows])

