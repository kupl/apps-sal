def any_arrows(arrows):
    for i in arrows:
        if 'damaged' not in i.keys() or ('damaged' in i.keys() and i['damaged'] == False):
            return True
    return False
