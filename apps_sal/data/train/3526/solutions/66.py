def any_arrows(arrows):
    print(arrows)
    for el in arrows:
        if el.get('damaged') != True:
            return True
    return False
