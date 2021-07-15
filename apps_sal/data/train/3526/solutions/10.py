def any_arrows(arrows):
    return not all(map(lambda x: x['damaged'] if 'damaged' in x else False, arrows))
