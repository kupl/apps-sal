def any_arrows(arrows):
    return bool([ arrow for arrow in arrows if not arrow.get('damaged', False) ])
