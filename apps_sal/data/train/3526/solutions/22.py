def any_arrows(arrows):
    return not all(map(lambda d: d.get('damaged', False), arrows)) if arrows else False
