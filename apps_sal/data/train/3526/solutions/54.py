def any_arrows(arrows):
    return any(('damaged' not in arrow or arrow['damaged'] == False for arrow in arrows))
