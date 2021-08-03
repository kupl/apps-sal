def any_arrows(arrows):
    if arrows:
        for arrow in arrows:
            if arrow.get('damaged'):
                continue
            else:
                return True
        return False
    else:
        return False
