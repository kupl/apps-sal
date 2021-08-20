def any_arrows(arrows):
    return any([not x['damaged'] if 'damaged' in x else True for x in arrows])
