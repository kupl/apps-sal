def any_arrows(arrows):
    return bool([x for x in arrows if not x.setdefault('damaged', False)])
