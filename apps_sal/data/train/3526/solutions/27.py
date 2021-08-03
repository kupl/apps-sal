def any_arrows(arrows):
    for dct in arrows:
        if 'damaged' not in dct.keys() or dct['damaged'] == False:
            return True
    return False
