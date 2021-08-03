def any_arrows(arrows):
    print(arrows)
    left = False
    if arrows == []:
        return False

    for status in arrows:
        if 'damaged' not in status:
            return True
        else:
            if status['damaged'] is not True:
                return True
    return False
