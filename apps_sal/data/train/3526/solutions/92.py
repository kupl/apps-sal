def any_arrows(arrows):
    return any(arrow for arrow in arrows if 'damaged' not in arrow or not bool(arrow['damaged']))
