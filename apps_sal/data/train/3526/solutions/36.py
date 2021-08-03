def any_arrows(arrows):
    status = [i.get('damaged') for i in arrows if 'damaged' in i]
    return not sum(status) == len(arrows)
