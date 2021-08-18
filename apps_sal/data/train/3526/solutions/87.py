def any_arrows(arrows):
    try:
        return min(i.get('damaged', 0) for i in arrows) == 0
    except:
        return False
