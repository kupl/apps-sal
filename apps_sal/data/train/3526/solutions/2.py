def any_arrows(arrows):
    return any([True for a in arrows if 'damaged' not in a or a['damaged'] == False])
