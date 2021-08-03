def any_arrows(arrows):
    for arr in arrows:
        if not ('damaged' in arr and arr['damaged']):
            return True
    return False
