def any_arrows(arrows):
    return any([x for x in arrows if (True if ('damaged' not in list(x.keys()) or (x['damaged'] is False)) else False)])

