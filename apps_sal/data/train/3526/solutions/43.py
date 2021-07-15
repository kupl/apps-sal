def any_arrows(arrows):
    return len([arrow for arrow in arrows if arrow.get('damaged') != True]) > 0
