def any_arrows(arrows):
    for obj in arrows:
        if obj.get('damaged', False) == False:
            return True
    return False
