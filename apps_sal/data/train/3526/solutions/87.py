def any_arrows(arrows):
    # your code here
    try:
        return min(i.get('damaged', 0) for i in arrows) == 0
    except:
        return False
