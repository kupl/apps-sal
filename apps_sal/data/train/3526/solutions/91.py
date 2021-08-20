def any_arrows(arrows):
    return any((arrow for arrow in arrows if not arrow.get('damaged', False)))
