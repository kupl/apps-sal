def any_arrows(arrows):
    try:
        for i in arrows:
            if 'damaged' in i:
                if i['damaged'] == False:
                    return True
            else:
                return True
        return False
    except:
        return False
