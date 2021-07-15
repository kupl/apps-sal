def any_arrows(arrows):
    for arrow in arrows:
        try:
            if arrow['damaged']:
                continue
        except KeyError:
            return True
        else: return True
    return False
