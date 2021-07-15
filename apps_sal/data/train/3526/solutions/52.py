def any_arrows(arrows):
    for arr in arrows:
        if 'damaged' in arr:
           if arr['damaged'] == False :
                return True
        else:
            return True
    return False
