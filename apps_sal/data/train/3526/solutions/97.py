def any_arrows(arrows):
    for obj in arrows:
        if not ('damaged' in obj and obj['damaged']):
            return True
    return False
